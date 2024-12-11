# PlayerController.py
from Model.Cell import Cell
from Model.Pawn import Pawn
from View.GridView import GridView

class PlayerController:
    def __init__(self, root, grid):
        self.view = GridView(root, self)
        self.grid = grid
        self.view.draw_grid(self.grid)
        self.last_pawn_clicked = None

    def test_button(self):
        new_cell = random.choice(random.choice(self.grid.cells))
        pawn = random.choice(self.grid.pawns)
        self.move_pawn(pawn, new_cell)

    def move_pawn(self, pawn: Pawn, dest_cell: Cell):
        old_cell = pawn.cell
        pawn.cell = dest_cell
        self.light_off_cells()
        self.view.move_pawn(old_cell, pawn)
        self.last_pawn_clicked = None

    def find_possibles_moves(self, pawn: Pawn) -> [Cell]:
        moves_list: [Cell] = []

        row_pawn, col_pawn = pawn.cell.row, pawn.cell.col

        # North
        i = 0
        stop = False
        while not stop:
            check_row = row_pawn - i
            if check_row == 0 or self.grid.cells[check_row][col_pawn].walls['N']:
                stop = True
                moves_list.append(self.grid.cells[check_row][col_pawn])
            else:
                for other_pawn in self.grid.pawns:
                    if pawn != other_pawn:
                        if self.grid.cells[check_row - 1][col_pawn] == other_pawn.cell:
                            stop = True
                            moves_list.append(self.grid.cells[check_row][col_pawn])
            i += 1

        # South
        i = 0
        stop = False
        while not stop:
            check_row = row_pawn + i
            if check_row == 15 or self.grid.cells[check_row][col_pawn].walls['S']:
                stop = True
                moves_list.append(self.grid.cells[check_row][col_pawn])
            else:
                for other_pawn in self.grid.pawns:
                    if pawn != other_pawn:
                        if self.grid.cells[check_row + 1][col_pawn] == other_pawn.cell:
                            stop = True
                            moves_list.append(self.grid.cells[check_row][col_pawn])
            i += 1

        # West
        i = 0
        stop = False
        while not stop:
            check_col = col_pawn - i
            if check_col == 0 or self.grid.cells[row_pawn][check_col].walls['W']:
                stop = True
                moves_list.append(self.grid.cells[row_pawn][check_col])
            else:
                for other_pawn in self.grid.pawns:
                    if pawn != other_pawn:
                        if self.grid.cells[row_pawn][check_col - 1] == other_pawn.cell:
                            stop = True
                            moves_list.append(self.grid.cells[row_pawn][check_col])
            i += 1

        # East
        i = 0
        stop = False
        while not stop:
            check_col = col_pawn + i
            if check_col == 15 or self.grid.cells[row_pawn][check_col].walls['E']:
                stop = True
                moves_list.append(self.grid.cells[row_pawn][check_col])
            else:
                for other_pawn in self.grid.pawns:
                    if pawn != other_pawn:
                        if self.grid.cells[row_pawn][check_col + 1] == other_pawn.cell:
                            stop = True
                            moves_list.append(self.grid.cells[row_pawn][check_col])
            i += 1

        # Erase useless moves
        final_moves_list = []
        for i in range(len(moves_list)):
            if pawn.cell != moves_list[i]:
                final_moves_list.append(moves_list[i])

        return final_moves_list

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

    def light_off_cells(self):
        for i in range(len(self.grid.cells)):
            for j in range(len(self.grid.cells)):
                if self.grid.cells[i][j].is_highlight:
                    self.grid.cells[i][j].is_highlight = False
                    self.view.update_cell(self.grid.cells[i][j])