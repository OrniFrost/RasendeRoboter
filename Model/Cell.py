class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {'N': False, 'E': False, 'S': False, 'W': False}
        self.item = (None,None)
        self.is_highlight = False

    def reset_walls(self):
        for wall in self.walls:
            self.walls[wall] = False

    def __str__(self):
        return f"Cell ({self.row}, {self.col}) - Walls: {self.walls} - Item: {self.item} - Highlight: {self.is_highlight}"