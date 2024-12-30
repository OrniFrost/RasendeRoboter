# PlayerController.py
import random
from tkinter import BooleanVar

from Controller.BaseActionController import BaseActionController


class PlayerController(BaseActionController):
    def __init__(self, root, grid, view):
        super().__init__(root, grid, view)
        view.instanciate_buttons(self)
        self.is_not_playing = BooleanVar()
        self.is_not_playing.set(True)

    def skip_button(self):
        # new_cell = random.choice(random.choice(self.grid.cells))
        # pawn = random.choice(self.grid.pawns)
        # self.move_pawn(pawn, new_cell)
        self.is_not_playing.set(True)
        self.reset_moves_counter()

    def make_turn(self, target):
        self.view.reset_moves_counter()
        self.is_not_playing.set(False)
        self.check_end_turn(target)
        self.root.wait_variable(self.is_not_playing)

    def check_end_turn(self, target):
        if not self.test_end_turn(target):
            # print("Turn not ended yet")
            self.root.after(100, self.check_end_turn, target)  # Check again after 100ms
        else:
            self.is_not_playing.set(True)
            print("Turn ended successfully")
