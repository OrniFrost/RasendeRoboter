from multiprocessing.reduction import duplicate

from Model import Cell, Pawn


class Grid:
    def __init__(self, tile_1, tile_2, tile_3, tile_4):
        self.cells: [[Cell]] = []
        self.pawns: [Pawn] = None
        for i in range(16):
            row = []
            for j in range(16):
                cell = None
                if i < 8 and j < 8:
                    cell = tile_1[i][j]
                elif i < 8 and j >= 8:
                    cell = tile_2[i][j-8]
                elif i >= 8 and j < 8:
                    cell = tile_4[i-8][j]
                else :
                    cell =tile_3[i-8][j-8]

                cell.row = i
                cell.col = j
                row.append(cell)
            self.cells.append(row)

        self.double_walls()

    def double_walls(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells)):
                #Check North
                if i != 0 and self.cells[i][j].walls['N']:
                    self.cells[i - 1][j].walls['S'] = True

                # Check East
                if j != 15 and self.cells[i][j].walls['E']:
                    self.cells[i][j + 1].walls['W'] = True

                # Check South
                if i != 15 and self.cells[i][j].walls['S']:
                    self.cells[i + 1][j].walls['N'] = True

                # Check West
                if j != 0 and self.cells[i][j].walls['W']:
                    self.cells[i][j - 1].walls['E'] = True

    def find_cell_of_target(self, target: (str,str)) -> Cell:
        for i in range(len(self.cells)):
            for j in range(len(self.cells)):
                if self.cells[i][j].item == target:
                    cell_of_the_target = self.cells[i][j]
        return  cell_of_the_target

    def test_pawn_is_on_target(self, target: (str,str)) -> bool:
        if target != ("black", "hole"):
            if self.get_pawn_of_a_target(target).cell == self.find_cell_of_target(target):
                return True
        else :
            for pawn in self.pawns:
                if pawn.cell == self.find_cell_of_target(target):
                    return True
        return False

    def get_pawn_of_a_target(self, target : (str,str)) -> Pawn :
        for pawn in self.pawns:
            if pawn.color == target[0]:
                pawn_target = pawn
        return pawn_target

    def find_possible_moves(self, pawn: Pawn, pawns : [Pawn]) -> [Cell]:
        moves_list: [Cell] = []

        row_pawn, col_pawn = pawn.cell.row, pawn.cell.col

        # North
        i = 0
        stop = False
        while not stop:
            check_row = row_pawn - i
            if check_row == 0 or self.cells[check_row][col_pawn].walls['N']:
                stop = True
                moves_list.append(self.cells[check_row][col_pawn])
            else:
                for other_pawn in pawns:
                    if pawn != other_pawn:
                        if self.cells[check_row - 1][col_pawn] == other_pawn.cell:
                            stop = True
                            moves_list.append(self.cells[check_row][col_pawn])
            i += 1

        # South
        i = 0
        stop = False
        while not stop:
            check_row = row_pawn + i
            if check_row == 15 or self.cells[check_row][col_pawn].walls['S']:
                stop = True
                moves_list.append(self.cells[check_row][col_pawn])
            else:
                for other_pawn in pawns:
                    if pawn != other_pawn:
                        if self.cells[check_row + 1][col_pawn] == other_pawn.cell:
                            stop = True
                            moves_list.append(self.cells[check_row][col_pawn])
            i += 1

        # West
        i = 0
        stop = False
        while not stop:
            check_col = col_pawn - i
            if check_col == 0 or self.cells[row_pawn][check_col].walls['W']:
                stop = True
                moves_list.append(self.cells[row_pawn][check_col])
            else:
                for other_pawn in pawns:
                    if pawn != other_pawn:
                        if self.cells[row_pawn][check_col - 1] == other_pawn.cell:
                            stop = True
                            moves_list.append(self.cells[row_pawn][check_col])
            i += 1

        # East
        i = 0
        stop = False
        while not stop:
            check_col = col_pawn + i
            if check_col == 15 or self.cells[row_pawn][check_col].walls['E']:
                stop = True
                moves_list.append(self.cells[row_pawn][check_col])
            else:
                for other_pawn in pawns:
                    if pawn != other_pawn:
                        if self.cells[row_pawn][check_col + 1] == other_pawn.cell:
                            stop = True
                            moves_list.append(self.cells[row_pawn][check_col])
            i += 1

        # Erase useless moves
        final_moves_list = []
        for i in range(len(moves_list)):
            if pawn.cell != moves_list[i]:
                final_moves_list.append(moves_list[i])

        return final_moves_list