class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {'N': False, 'E': False, 'S': False, 'W': False}
        self.item = (None,None)

    def reset_walls(self):
        for wall in self.walls:
            self.walls[wall] = False