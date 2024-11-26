class Grid:
    def __init__(self, tile_1, tile_2, tile_3, tile_4):
        self.cells = []
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