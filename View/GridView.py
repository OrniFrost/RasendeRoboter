# GridView.py
import tkinter as tk
from tkinter import ttk

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

        self.button_test = ttk.Button(self.buttons_frame, text="Test", command=self.controller.test_button)
        self.button_test.grid(row=0, column=0)

        self.grid_cells_view: [[CellView]] = []

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
        print(len(self.grid_cells_view),row,col)
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
