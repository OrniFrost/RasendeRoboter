# GridView.py
import tkinter as tk
from time import sleep
from tkinter import ttk

from Controller.BaseActionController import BaseActionController
from Model.Cell import Cell
from Model.Pawn import Pawn
from View.CellView import CellView


class GridView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.grid_frame = ttk.Frame(self.main_frame)
        self.grid_frame.grid(row=0, column=0, padx=5, pady=5)

        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

        self.grid_cells_view: [[CellView]] = []

        self.moves_counter = 0

    def draw_grid(self, grid):
        print("draw_grid")
        for i in range(len(grid.cells)):
            row_view: [CellView] = []
            for j in range(len(grid.cells)):
                cell = grid.cells[i][j]
                cell_view = CellView(self.grid_frame, cell)
                cell_view.draw()
                cell_view.canvas.bind('<Button-1>', lambda event, cell_clicked = cell: self.controller.click_on_cell(cell_clicked))

                row_view.append(cell_view)
            self.grid_cells_view.append(row_view)

        for pawn in grid.pawns:
            self.draw_pawn(pawn)

    def draw_pawn(self,pawn: Pawn):
        row,col = pawn.cell.row, pawn.cell.col
        cell_view = self.grid_cells_view[row][col]
        cell_view.canvas.create_polygon(cell_view.polygon_pawn, fill=pawn.color, outline='black', width=2)

    def move_pawn(self,old_cell: Cell, pawn: Pawn):
        old_row, old_col = old_cell.row, old_cell.col
        self.grid_cells_view[old_row][old_col].draw()

        self.draw_pawn(pawn)

    def update_cells(self, cells_list: [Cell]):
        for cell in cells_list:
            self.update_cell(cell)

    def update_cell(self,cell: Cell):
        self.grid_cells_view[cell.row][cell.col].draw()

    def instanciate_buttons(self, controller : BaseActionController):

        self.round_number_label = ttk.Label(self.buttons_frame, text="Round Number: 1")
        self.round_number_label.grid(row=0, column=0, pady=5)

        self.player_points_label = ttk.Label(self.buttons_frame, text="Player: 0")
        self.player_points_label.grid(row=1, column=1, pady=5)

        self.ai_points_label = ttk.Label(self.buttons_frame, text="AI: 0")
        self.ai_points_label.grid(row=1, column=0, pady=5)

        self.target_label = ttk.Label(self.buttons_frame, text="Actual target : ")
        self.target_label.grid(row=2, column=0, pady=5)

        self.turn_label = ttk.Label(self.buttons_frame, text="Turn : Player")
        self.turn_label.grid(row=3, column=0, pady=5)

        self.button_test = ttk.Button(self.buttons_frame, text="Skip turn", command=self.controller.skip_button)
        self.button_test.grid(row=4, column=0, pady=5)

        self.moves_counter_label = ttk.Label(self.buttons_frame, text="Moves counter : 0")
        self.moves_counter_label.grid(row=5, column=0, pady=5)

    def actualize_round(self, number, target):
        self.round_number_label.config(text=f"Round Number : {number}")
        self.target_label.config(text=f"Actual target : {target[0]} {target[1]}")

    def update_scores(self,ai_score: int, player_score: int):
        self.ai_points_label.config(text=f"AI: {ai_score}")
        self.player_points_label.config(text=f"Player: {player_score}")

    def actualize_turn(self, player: str):
        self.turn_label.config(text=f"Turn : {player}")

    def increment_moves_counter(self):
        self.moves_counter += 1
        self.moves_counter_label.config(text=f"Moves counter : {self.moves_counter}")

    def reset_moves_counter(self):
        self.moves_counter = 0
        self.moves_counter_label.config(text=f"Moves counter : {self.moves_counter}")

    def test_cell(self, cell: Cell):
        self.grid_cells_view[cell.row][cell.col].canvas.create_rectangle(15,15,35,35, fill='brown')