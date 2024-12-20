import math
import tkinter
from random import randint
from time import sleep

from Controller.BaseActionController import BaseActionController
import random

from Model.Cell import Cell
from Model.Grid import Grid
from Model.Node import Node
from Model.Pawn import Pawn


class AIController(BaseActionController):
    def __init__(self, root, grid, view):
        super().__init__(root, grid, view)

    def make_turn(self, target):
        # Implement AI logic here
        moves = self.a_star_one_pawn(target)
        print(moves)
        if moves is not None:
            for move in moves:
                self.move_pawn(move[0],move[1])
                print(move[0],move[1])
                var = tkinter.IntVar()
                self.root.after(500, var.set, 1)
                self.root.wait_variable(var)

    def generate_random_move(self) -> [(Pawn, Cell)]:
        ai_moves = []
        for i in range(randint(2, 5)):
            pawn = random.choice(self.grid.pawns)
            cell: Cell = random.choice(self.find_possibles_moves(pawn))
            ai_moves.append((pawn,cell))
        return ai_moves

    def a_star_one_pawn(self, target : (str,str)):
        pawn_target: Pawn = self.grid.get_pawn_of_a_target(target)
        start_node : Node = Node(self.grid, None, 0, 0)
        open_list : [Node] = [start_node]
        closed_list : [Node] = []

        final_node : Node = None
        while len(open_list) != 0:
            # Retirer le node avec la value mini
            min_val = 100000
            idx = 0
            for i in range(len(open_list)):
                if open_list[i].value_f <  min_val:
                    min_val = open_list[i].value_f
                    idx = i

            node: Node = open_list.pop(idx)
            print(node)
            # Vérif si node est la solution
            if node.state.test_pawn_is_on_target(target):
                print("pawn is on target")
                final_node = node
                break

            closed_list.append(node)

            for next_cell in node.state.find_possible_moves(pawn_target):
                print("next_cell", next_cell.row, next_cell.col)
                n_prime = Node(node.state, node, 0, 0) # A vérifier les instances
                self.move_pawn_node(n_prime, next_cell, target)

                h_n_prime = self.h(n_prime, target)
                g_n_prime = node.value_g + 1

                f_n_prime = g_n_prime + h_n_prime
                n_prime.value_f = f_n_prime
                n_prime.value_g = g_n_prime
                
                test_list : [Node] = open_list + closed_list
                is_in_test_list = True
                is_inf = True
                # for n_test in test_list:
                #     if self.nodes_are_equals(n_prime,n_test) :
                #         is_in_test_list = False
                is_in_test_list = n_prime in test_list

                if n_prime.value_g <= node.value_g:
                    is_inf = False

                print(is_in_test_list, is_inf)
                if not is_in_test_list and is_inf:
                    open_list.append(n_prime)
                    print(open_list)

        if not final_node:
            return None
        else:
            return self.find_travel_to_final_node(final_node,target)


    def find_travel_to_final_node(self, final_node : Node, target) -> (Pawn,Cell):
        moves_list: (Pawn,Cell) = []
        n : Node = final_node

        while n.father_state is not None:
            p: Pawn = n.state.get_pawn_of_a_target(target)
            moves_list.append((p, p.cell))
            n = n.father_state

        moves_list.reverse()
        return moves_list

    def h(self,node : Node, target : (str,str)):
        cell_pawn_target : Cell = node.state.get_pawn_of_a_target(target).cell
        cell_target : Cell = node.state.find_cell_of_target(target)
        return math.sqrt((cell_target.row - cell_pawn_target.row)**2 +
                         (cell_target.col - cell_pawn_target.col)**2)

    def nodes_are_equals(self, n1 : Node, n2 : Node):
        return n1 == n2

    def move_pawn_node(self, node: Node, dest_cell: Cell, target):
        node.state.get_pawn_of_a_target(target).cell = dest_cell
