from Model import Cell


class Pawn:
    def __init__(self,color, cell : Cell):
        self.color = color
        self.cell = cell

    def __str__(self):
        return f"{self.color} ({self.cell.row},{self.cell.col})"

    def __eq__(self, other):
        self_coord = self.cell.row, self.cell.col
        other_coord = other.cell.row, other.cell.col

        if self_coord != other_coord or self.color != other.color:
            return False
        return True