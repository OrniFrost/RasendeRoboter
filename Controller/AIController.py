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
        idx_pawn_target = self.find_index_pawn_of_target(target)
        start_node : Node = Node(self.grid.pawns, None, 0, 0)
        open_list : [Node] = [start_node]
        closed_list : [Node] = []

        final_node : Node = None
        while len(open_list) != 0:
            min_val = 1000000
            idx = 0
            for i in range(len(open_list)):
                if open_list[i].value_f < min_val:
                    min_val = open_list[i].value_f
                    idx = i

            n : Node = open_list.pop(idx)

            if n.state[idx_pawn_target].cell.item == target:
                final_node = n
                break



    def find_travel_to_final_node(self, final_node : Node, target) -> (Pawn,Cell):
        moves_list: (Pawn,Cell) = []
        n : Node = final_node

        while n.father_state is not None:
            p: Pawn = n.state.get_pawn_of_a_target(target)
            moves_list.append((p, p.cell))
            n = n.father_state

        moves_list.reverse()
        return moves_list

    def find_index_pawn_of_target(self, target : (str,str)) -> int:
        for i in range(len(self.grid.pawns)):
            if self.grid.pawns[i].color == target[0]:
                return i

    def h(self,node : Node, target : (str,str)):
        cell_pawn_target : Cell = node.state.get_pawn_of_a_target(target).cell
        cell_target : Cell = node.state.find_cell_of_target(target)
        return math.sqrt((cell_target.row - cell_pawn_target.row)**2 +
                         (cell_target.col - cell_pawn_target.col)**2)

    def nodes_are_equals(self, n1 : Node, n2 : Node):
        return n1 == n2

    def move_pawn_node(self, node: Node, dest_cell: Cell, target):
        node.state.get_pawn_of_a_target(target).cell = dest_cell
