from Model.Grid import Grid
from Model.Pawn import Pawn


class Node:

    def __init__(self, state : [Pawn], father_state, value_f : float, value_g: int):
        self.state = state
        self.father_state = father_state
        self.value_f = value_f
        self.value_g = value_g

    def __eq__(self, other):
        for i in range(len(self.state)):
            p1_coord = self.state[i].cell.row, self.state[i].cell.col
            p2_coord = other.state[i].cell.row, other.state[i].cell.col
            if p1_coord != p2_coord:
                return False
        return True

    def __lt__(self, other):
        return self.value_f < other.value_f

    def __str__(self):
        string = ""
        for p in self.state:
            string += str(p) + "\n"
        return string