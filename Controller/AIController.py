import tkinter
from random import randint
from time import sleep

from Controller.BaseActionController import BaseActionController
import random

from Model.Cell import Cell
from Model.Pawn import Pawn


class AIController(BaseActionController):
    def __init__(self, root, grid, view):
        super().__init__(root, grid, view)

    def make_turn(self, target):
        # Implement AI logic here
        for move in self.generate_random_move():
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

