import random

from Model.Cell import Cell
from Model.Grid import Grid
from View.View import GridView

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
        self.view.draw_grid(self.grid)

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

    def test_button(self):
        print("okay lezgo")