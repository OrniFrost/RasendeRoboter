import random

from Model.Cell import Cell
from Model.Grid import Grid
from Model.Pawn import Pawn
from View.GridView import GridView

items_list = [
    ("blue", "circle"),
    ("blue", "square"),
    ("blue", "triangle"),
    ("blue", "star"),
    ("red", "circle"),
    ("red", "square"),
    ("red", "triangle"),
    ("red", "star"),
    ("yellow", "circle"),
    ("yellow", "square"),
    ("yellow", "triangle"),
    ("yellow", "star"),
    ("green", "circle"),
    ("green", "square"),
    ("green", "triangle"),
    ("green", "star")
]

class Controller:
    def __init__(self, root):
        self.view = GridView(root, self)
        self.tiles = [self.build_tile_1(), self.build_tile_2(), self.build_tile_3(), self.build_tile_4()]
        random.shuffle(self.tiles)
        for i in range(1, 4):
            self.tiles[i] = self.rotate_tile_clockwise(self.tiles[i], i)
        self.grid = Grid(self.tiles[0], self.tiles[1], self.tiles[2], self.tiles[3])



        colors_list = ["blue","green","red","yellow"]
        pawns_list = []
        [pawns_list.append(Pawn(colors_list.pop(0),cell)) for cell in self.find_random_cells_starts_for_pawns()]
        self.grid.pawns = pawns_list

        self.view.draw_grid(self.grid)

        self.find_possibles_moves(self.grid.pawns[0])
        self.last_pawn_clicked = None

    def create_tile(self, size):
        tile = []
        for i in range(size):
            tile.append([])
            for j in range(size):
                tile[i].append(Cell(i, j))
        tile[7][6].walls['E'] = True
        tile[6][7].walls['S'] = True
        return tile

    def build_tile_1(self):
        tile = self.create_tile(8)
        tile[0][3].walls['E'] = True
        tile[1][5].walls['E'] = True
        tile[1][6].walls['S'] = True
        tile[2][1].walls['S'] = True
        tile[3][1].walls['E'] = True
        tile[3][5].walls['S'] = True
        tile[4][4].walls['E'] = True
        tile[5][2].walls['E'] = True
        tile[5][2].walls['S'] = True
        tile[5][7].walls['E'] = True
        tile[5][7].walls['S'] = True
        tile[6][0].walls['S'] = True

        tile[1][6].item = items_list[0]
        tile[3][1].item = items_list[10]
        tile[4][5].item = items_list[13]
        tile[5][2].item = items_list[7]

        return tile

    def build_tile_2(self):
        tile = self.create_tile(8)
        tile[0][3].walls['E'] = True
        tile[1][5].walls['E'] = True
        tile[1][5].walls['S'] = True
        tile[2][0].walls['E'] = True
        tile[2][1].walls['S'] = True
        tile[3][0].walls['S'] = True
        tile[3][6].walls['S'] = True
        tile[4][5].walls['E'] = True
        tile[5][2].walls['S'] = True
        tile[6][2].walls['E'] = True

        tile[1][5].item = items_list[15]
        tile[2][1].item = items_list[5]
        tile[4][6].item = items_list[8]
        tile[6][2].item = items_list[2]

        return tile

    def build_tile_3(self):
        tile = self.create_tile(8)
        tile[0][3].walls['E'] = True
        tile[1][0].walls['E'] = True
        tile[1][1].walls['S'] = True
        tile[1][6].walls['S'] = True
        tile[2][6].walls['E'] = True
        tile[4][2].walls['E'] = True
        tile[4][2].walls['S'] = True
        tile[4][7].walls['S'] = True
        tile[5][0].walls['S'] = True
        tile[5][6].walls['E'] = True

        tile[1][1].item = items_list[6]
        tile[2][6].item = items_list[12]
        tile[4][2].item = items_list[3]
        tile[5][7].item = items_list[9]

        return tile

    def build_tile_4(self):
        tile = self.create_tile(8)
        tile[0][2].walls['E'] = True
        tile[0][4].walls['S'] = True
        tile[1][1].walls['S'] = True
        tile[1][3].walls['E'] = True
        tile[2][1].walls['E'] = True
        tile[3][6].walls['E'] = True
        tile[3][6].walls['S'] = True
        tile[5][0].walls['S'] = True
        tile[6][2].walls['E'] = True
        tile[6][3].walls['S'] = True

        tile[1][4].item = items_list[5]
        tile[2][1].item = items_list[14]
        tile[3][6].item = items_list[11]
        tile[6][3].item = items_list[1]

        return tile

    def rotate_tile_clockwise(self, tile, times):
        for _ in range(times):
            new_tile = [[Cell(i, j) for j in range(len(tile))] for i in range(len(tile))]
            for i in range(len(tile)):
                for j in range(len(tile)):
                    row, col = tile[i][j].row, tile[i][j].col
                    walls = tile[row][col].walls
                    new_col_index = len(tile) - 1 - i
                    if walls['N']:
                        new_tile[j][new_col_index].walls['E'] = True
                    if walls['E']:
                        new_tile[j][new_col_index].walls['S'] = True
                    if walls['S']:
                        new_tile[j][new_col_index].walls['W'] = True
                    if walls['W']:
                        new_tile[j][new_col_index].walls['N'] = True
                    new_tile[j][new_col_index].item = tile[row][col].item
            tile = new_tile
        return tile

    def find_random_cells_starts_for_pawns(self) -> [Cell]:
        cells_list: [Cell] = []
        while len(cells_list) != 4:
            row,col = random.randint(0,15), random.randint(0,15)
            middle = [7,8]
            if row not in middle and col not in middle:
                if self.grid.cells[row][col].item == (None,None):
                    is_okay = True
                    for cell in cells_list :
                        r,c = cell.row, cell.col
                        if row == r and col == c:
                            is_okay = False
                    if is_okay:
                        cells_list.append(self.grid.cells[row][col])
        return cells_list

    def test_button(self):
        new_cell = random.choice(random.choice(self.grid.cells))
        pawn = random.choice(self.grid.pawns)
        self.move_pawn(pawn, new_cell)

    def move_pawn(self, pawn: Pawn, dest_cell: Cell):
        old_cell = pawn.cell
        pawn.cell = dest_cell
        self.light_off_cells()
        self.view.move_pawn(old_cell,pawn)
        self.last_pawn_clicked = None

    def find_possibles_moves(self, pawn: Pawn) -> [Cell]:
        moves_list: [Cell] = []

        row_pawn, col_pawn = pawn.cell.row, pawn.cell.col

        #North
        i = 0
        stop = False
        while not stop:
            check_row = row_pawn - i
            if check_row == 0 or self.grid.cells[check_row][col_pawn].walls['N'] :
                stop = True
                moves_list.append(self.grid.cells[check_row][col_pawn])
            else:
                for other_pawn in self.grid.pawns :
                    if pawn != other_pawn :
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
        for pawn in self.grid.pawns :
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