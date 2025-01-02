# CellView.py
import tkinter as tk
from tkinter import ttk

class CellView:
    polygon_pawn = [9, 46, 13, 41, 11, 36, 8, 33, 8, 29, 11, 26, 15, 23, 13, 20, 11, 18, 10, 16, 10, 12, 12, 9, 15, 7,
                    19, 5, 30, 5, 34, 7, 37, 9, 39, 12, 39, 16, 38, 18, 36, 20, 34, 23, 38, 26, 41, 29, 41, 33, 38, 36,
                    36, 41, 38, 46]
    polygon_star = [5,45,15,28,5,19,16,14,24,3,25,3,33,14,44,19,34,28,44,45,25,37,24,37]

    def __init__(self, parent, cell):
        self.cell = cell
        self.frame = ttk.Frame(parent)
        self.frame.grid(row=cell.row, column=cell.col)
        self.canvas = tk.Canvas(self.frame, width=50, height=50, bg='white', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_rectangle(0, 0, 50, 50, width=0.1)

    def draw(self):
        self.canvas.delete("all")  # Clear the canvas
        color = "light green" if self.cell.is_highlight else "white"
        self.canvas.create_rectangle(0, 0, 50, 50, width=0.1, fill=color)
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
            if item == ("black", "hole"):
                self.canvas.create_oval(10, 10, 40, 40, fill=color, outline='')

                self.canvas.create_oval(5, 5, 45, 45, outline='black')
                self.canvas.create_oval(7, 7, 43, 43, outline='black')

                self.canvas.create_polygon([20,45,10,40,5,30,21,28,24,37], fill="blue", outline='')

                self.canvas.create_polygon([5,19,10,9,20,4,21,21,13,24], fill="green", outline='')

                self.canvas.create_polygon([29,4,39,9,44,19,28,21,25,13], fill="yellow", outline='')

                self.canvas.create_polygon([44,30,39,40,29,45,28,28,37,25], fill="red", outline='')
            else:
                match item[1]:
                    case "circle":
                        self.canvas.create_oval(10, 10, 40, 40, fill=color, outline='')
                    case "square":
                        self.canvas.create_rectangle(10, 10, 40, 40, fill=color, outline='')
                    case "triangle":
                        self.canvas.create_polygon([25, 10, 10, 40, 40, 40], fill=color, outline='')
                    case "star":
                        self.canvas.create_polygon(self.polygon_star, fill=color, outline='')