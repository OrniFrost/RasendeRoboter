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

    def calculate_turn(self, target : (str,str), level: str) -> [(Pawn,Cell)]:
        if level == "easy":
            return self.calculate_turn_easy(target)
        else:
            return self.calculate_turn_medium(target)

    def calculate_turn_easy(self, target : (str,str)) -> [(Pawn,Cell)]:
        if target != ("black", "hole"):
            moves = self.a_star_one_pawn(
                idx_pawn_target=self.find_index_pawn_of_target(target),
                cell_target=self.grid.find_cell_of_target(target)
            )
        else:
            moves_list = []
            for i in range(4):
                moves_list.append(self.a_star_one_pawn(
                    idx_pawn_target=i,
                    cell_target=self.grid.find_cell_of_target(target)
                ))
            final_moves = moves_list[0]
            for m in moves_list:
                if m is not None:
                    if final_moves is None:
                        final_moves = m
                        continue
                    if len(m) < len(final_moves):
                        final_moves = m
            moves = final_moves
        return moves

    def calculate_turn_medium(self, target: (str, str)) -> [(Pawn, Cell)]:
        moves_list: [[(Pawn, Cell)]] = []
        if target != ("black", "hole"):
            moves_list.append(self.a_star_one_pawn(
                idx_pawn_target=self.find_index_pawn_of_target(target),
                cell_target=self.grid.find_cell_of_target(target)
                )
            )
            for idx_pawn in range(len(self.grid.pawns)):
                if self.grid.pawns[idx_pawn].color == target[0]:
                    continue
                for cell in self.grid.find_possible_moves(self.grid.pawns[idx_pawn], self.grid.pawns):
                    self.grid.pawns[idx_pawn].cell = cell
                    moves: [(Pawn, Cell)] = self.a_star_one_pawn(
                        idx_pawn_target=self.find_index_pawn_of_target(target),
                        cell_target=self.grid.find_cell_of_target(target)
                    )
                    if moves is not None:
                        moves.insert(0,(self.grid.pawns[idx_pawn], cell))

                    moves_list.append(moves)
        else :
            #Copy initial states of pawns
            pawns_start_pose: [Pawn] = [Pawn(p.color, p.cell) for p in self.grid.pawns]
            for i_pawns in range(len(self.grid.pawns)):
                moves_list.append(self.a_star_one_pawn(i_pawns, self.grid.find_cell_of_target(target)))
                for j_pawns in range(len(self.grid.pawns)):
                    if i_pawns == j_pawns:
                        continue
                    # Replace pawns to start pose
                    for i in range(len(pawns_start_pose)):
                        self.grid.pawns[i].cell = pawns_start_pose[i].cell

                    for cell in self.grid.find_possible_moves(self.grid.pawns[j_pawns], self.grid.pawns):
                        self.grid.pawns[j_pawns].cell = cell
                        moves: [(Pawn, Cell)] = self.a_star_one_pawn(
                            idx_pawn_target=i_pawns,
                            cell_target=self.grid.find_cell_of_target(target)
                        )
                        if moves is not None:
                            moves.insert(0, (self.grid.pawns[j_pawns], cell))

                        moves_list.append(moves)

        final_moves: [(Pawn, Cell)] = moves_list[0]
        for moves in moves_list :
            if moves is not None:
                if final_moves is None:
                    final_moves = moves
                    continue
                if len(moves) < len(final_moves):
                    final_moves = moves

        return final_moves

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

        while len(open_list) != 0: # While open list is not empty

            open_list.sort() # Sort open_list to have the node with the lowest value_f

            n : Node = open_list.pop(0)

            closed_list.append(n)

            if n.state[idx_pawn_target].cell == cell_target: # If this node is the target
                final_node = n
                return self.find_travel_to_final_node(final_node, idx_pawn_target) # Reassemble the path to the target

            pawn = n.state[idx_pawn_target]
            # For each cell on which the pawn can move
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

                if not (is_in_closed_list or is_in_open_list_with_inf_value): # Condition found on the A*'s wiki
                    h_y = self.h_manhattan_distance(p.cell, cell_target)

                    f_y = g_y + h_y

                    y.value_f = f_y
                    y.value_g = g_y

                    open_list.append(y)

        return None # No path found


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

    def h_euclidian_distance(self, cell_1 : Cell, cell_2 : Cell) -> float:
        return math.sqrt(
            (cell_2.row - cell_1.row)**2 + (cell_2.col - cell_1.col)**2
        )

    def h_manhattan_distance(self, cell_1 : Cell, cell_2 : Cell) -> float:
        return abs(cell_2.row - cell_1.row) + abs(cell_2.col - cell_1.col)