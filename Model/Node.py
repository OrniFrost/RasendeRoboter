from Model.Grid import Grid


class Node:
    def __init__(self, state : Grid, father_state, value_f : float, value_g : int):
        self.state = state
        self.father_state = father_state
        self.value_f = value_f
        self.value_g = value_g

    def __eq__(self, other):
        print("o")
        for p_i in self.state.pawns:
            p_i_coord = p_i.cell.row, p_i.cell.col
            for p_j in self.state.pawns:
                p_j_coord = p_j.cell.row, p_j.cell.col
                if p_i_coord != p_j_coord:
                    return False
        return True

    def __str__(self):
        return f"Node - {self.state.pawns[2].cell}"