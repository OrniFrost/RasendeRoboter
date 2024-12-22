from Model import Cell


class Pawn:
    def __init__(self,color, cell : Cell):
        self.color = color
        self.cell = cell

    def __str__(self):
        return f"{self.color} ({self.cell.row},{self.cell.col})"