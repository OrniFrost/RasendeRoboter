import tkinter

from Model import Grid
from Model.Cell import Cell
from Model.Pawn import Pawn
from View import GridView


class BaseActionController:
    def __init__(self, root : tkinter.Tk, grid : Grid, view: GridView):
        self.root = root
        self.view = view
        self.grid = grid
        self.view.controller = self  # Set the controller for GridView
        self.last_pawn_clicked = None
        self.moves_counter = 0
        # self.rounds_won = 0

    def move_pawn(self, pawn: Pawn, dest_cell: Cell):
        old_cell = pawn.cell
        pawn.cell = dest_cell
        self.light_off_cells()
        self.view.move_pawn(old_cell, pawn)
        self.last_pawn_clicked = None
        # self.moves_counter += 1

    def find_possibles_moves(self, pawn: Pawn) -> [Cell]:
        return self.grid.find_possible_moves(pawn, self.grid.pawns)

    def find_possibles_moves_with_specific_pawns(self, pawn: Pawn, pawns : [Pawn]) -> [Cell]:
        return self.grid.find_possible_moves(pawn, pawns)

    def click_on_cell(self, cell: Cell):
        print(cell.row, cell.col)

        pawn_clicked = None
        for pawn in self.grid.pawns:
            if pawn.cell == cell:
                pawn_clicked = pawn

        if pawn_clicked:
            self.last_pawn_clicked = pawn_clicked
            self.light_off_cells()
            moves_list = self.find_possibles_moves(pawn_clicked)
            for cell in moves_list:
                cell.is_highlight = True
                self.view.update_cell(cell)
        else:
            if cell.is_highlight:
                if self.last_pawn_clicked:
                    self.move_pawn(self.last_pawn_clicked, cell)
                    self.moves_counter += 1
                    print(f"move pawn {self.moves_counter}")
                    self.view.increment_moves_counter()

    def light_off_cells(self):
        for i in range(len(self.grid.cells)):
            for j in range(len(self.grid.cells)):
                if self.grid.cells[i][j].is_highlight:
                    self.grid.cells[i][j].is_highlight = False
                    self.view.update_cell(self.grid.cells[i][j])

    def test_end_turn(self, target : (str,str)) -> bool:
        if self.grid.test_pawn_is_on_target(target) :
            return True
        return False

    def reset_moves_counter(self):
        self.moves_counter = 0