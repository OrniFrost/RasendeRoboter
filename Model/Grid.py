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

    def find_cell_of_target(self, target: (str,str)):
        for i in range(len(self.cells)):
            for j in range(len(self.cells)):
                if self.cells[i][j].item == target:
                    cell_of_the_target = self.cells[i][j]
        return  cell_of_the_target