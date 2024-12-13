# PlayerController.py
import random

from Controller.BaseActionController import BaseActionController


class PlayerController(BaseActionController):
    def __init__(self, grid, view):
        super().__init__(grid, view)
        view.instanciate_buttons(self)

    def test_button(self):
        new_cell = random.choice(random.choice(self.grid.cells))
        pawn = random.choice(self.grid.pawns)
        self.move_pawn(pawn, new_cell)