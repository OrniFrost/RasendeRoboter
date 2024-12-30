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

    def calculate_turn(self, target) -> [(Pawn,Cell)]:

        if target != ("black","hole"):
            moves = self.a_star_one_pawn(
                    idx_pawn_target=self.find_index_pawn_of_target(target),
                    cell_target= self.grid.find_cell_of_target(target)
                )
        else :
            moves = None
            moves_list = []
            for i in range(4):
                moves_list.append(self.a_star_one_pawn(
                    idx_pawn_target=i,
                    cell_target=self.grid.find_cell_of_target(target)
                ))
            if len(moves_list) != 0:
                moves = moves_list.pop(0)
                for m in moves_list:
                    if m is not None :
                        if len(m) < len(moves):
                            moves = m

        return moves

    def make_turn(self, moves : [(Pawn, Cell)]):
        self.view.reset_moves_counter()
        self.wait(1000)
        if moves is not None:
            for move in moves:
                pawn_move : Pawn = move[0]
                for p in self.grid.pawns:
                    if pawn_move.color == p.color:
                        reel_pawn = p
                self.view.increment_moves_counter()
                self.wait(750)
                self.move_pawn(reel_pawn, move[1])

    def wait(self, ms: int):
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

    def a_star_one_pawn(self, idx_pawn_target : int, cell_target : Cell):

        start_node : Node = Node(self.grid.pawns, None, 0, 0)
        open_list : [Node] = [start_node]
        closed_list : [Node] = []

        while len(open_list) != 0:

            open_list.sort()

            n : Node = open_list.pop(0)

            closed_list.append(n)

            if n.state[idx_pawn_target].cell == cell_target:
                final_node = n
                return self.find_travel_to_final_node(final_node, idx_pawn_target)

            pawn = n.state[idx_pawn_target]
            for next_cell in self.find_possibles_moves_with_specific_pawns(pawn, n.state):
                y : Node = Node([Pawn(p.color,p.cell) for p in n.state], n, 0,0)
                p : Pawn = y.state[idx_pawn_target]
                p.cell = next_cell

                # self.view.test_cell(next_cell)

                g_y = n.value_g + 1

                is_in_closed_list : bool = y in closed_list
                is_in_open_list_with_inf_value : bool = False
                if y in open_list:
                    same_y = open_list[open_list.index(y)]
                    is_in_open_list_with_inf_value = same_y.value_g < g_y


                if not (is_in_closed_list or is_in_open_list_with_inf_value):
                    h_y = self.h(p.cell, cell_target)

                    f_y = g_y + h_y

                    y.value_f = f_y
                    y.value_g = g_y

                    open_list.append(y)

        return None


    def find_travel_to_final_node(self, final_node : Node, idx_pawn : int) -> [(Pawn,Cell)]:
        moves_list: (Pawn,Cell) = []
        n : Node = final_node

        while n.father_state is not None:
            p: Pawn = n.state[idx_pawn]
            moves_list.append((p, p.cell))
            n = n.father_state

        moves_list.reverse()
        return moves_list

    def find_index_pawn_of_target(self, target : (str,str)) -> int:
        for i in range(len(self.grid.pawns)):
            if self.grid.pawns[i].color == target[0]:
                return i

    def h(self, cell_1 : Cell, cell_2 : Cell) -> float:
        return math.sqrt(
            (cell_2.row - cell_1.row)**2 + (cell_2.col - cell_1.col)**2
        )
