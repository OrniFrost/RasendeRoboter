# CellView.py
import tkinter as tk
from tkinter import ttk

class CellView:
    polygon_pawn = [9,44,13,39,11,34,8,31,8,27,11,24,15,21,13,18,11,16,10,14,10,10,12,7,15,5,19,3,
                    30,3,34,5,37,7,39,10,39,14,38,16,36,18,34,21,38,24,41,27,41,31,38,34,36,39,38,44]

    def __init__(self, parent, cell):
        self.cell = cell
        self.frame = ttk.Frame(parent)
        self.frame.grid(row=cell.row, column=cell.col)
        self.canvas = tk.Canvas(self.frame, width=50, height=50, bg='white', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_rectangle(0, 0, 50, 50, width=0.1)

    def draw(self):
        self.canvas.delete("all")  # Clear the canvas
        self.canvas.create_rectangle(0, 0, 50, 50, width=0.1)
        walls = self.cell.walls
        if walls['N']:
            self.canvas.create_line(0, 0, 50, 0, width=5)
        if walls['E']:
            self.canvas.create_line(50, 0, 50, 50, width=5)
        if walls['S']:
            self.canvas.create_line(0, 50, 50, 50, width=5)
        if walls['W']:
            self.canvas.create_line(0, 0, 0, 50, width=5)

        item = self.cell.item
        if item != (None, None):
            color = item[0]
            match item[1]:
                case "circle":
                    self.canvas.create_oval(10, 10, 40, 40, fill=color, outline='')
                case "square":
                    self.canvas.create_rectangle(10, 10, 40, 40, fill=color, outline='')
                case "triangle":
                    self.canvas.create_polygon([25, 10, 10, 40, 40, 40], fill=color, outline='')
                case "star":
                    self.canvas.create_oval(10, 15, 40, 30, fill=color, outline='')