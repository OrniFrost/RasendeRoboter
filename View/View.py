import tkinter as tk
from tkinter import ttk

polygon_pawn = [9,44,13,39,11,34,8,31,8,27,11,24,15,21,13,18,11,16,10,14,10,10,12,7,15,5,19,3,
                30,3,34,5,37,7,39,10,39,14,38,16,36,18,34,21,38,24,41,27,41,31,38,34,36,39,38,44]

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

    def draw_grid(self, grid):
        for i in range(len(grid.cells)):
            for j in range(len(grid.cells)):
                cell = grid.cells[i][j]

                cell_frame = ttk.Frame(self.grid_frame)
                cell_frame.grid(row=i, column=j)

                cell_canvas = tk.Canvas(cell_frame, width=50, height=50, bg='white', highlightthickness=0)
                cell_canvas.pack(fill="both", expand=True)
                cell_canvas.create_rectangle(0, 0, 50, 50, width=0.1)

                text = cell.row, cell.col

                def print_test(event, text=text):
                    print(text)

                cell_canvas.bind('<Button-1>', print_test)

                walls = cell.walls
                if walls['N']:
                    cell_canvas.create_line(0, 0, 50, 0, width=5)
                if walls['E']:
                    cell_canvas.create_line(50, 0, 50, 50, width=5)
                if walls['S']:
                    cell_canvas.create_line(0, 50, 50, 50, width=5)
                if walls['W']:
                    cell_canvas.create_line(0, 0, 0, 50, width=5)

                item = cell.item
                if item != (None, None):
                    color = item[0]
                    match item[1]:
                        case "circle":
                            cell_canvas.create_oval(10, 10, 40, 40, fill=color, outline='')
                        case "square":
                            cell_canvas.create_rectangle(10, 10, 40, 40, fill=color, outline='')
                        case "triangle":
                            cell_canvas.create_polygon([25, 10, 10, 40, 40, 40], fill=color, outline='')
                        case "star":
                            cell_canvas.create_oval(10, 15, 40, 30, fill=color, outline='')

                for pawn in grid.pawns:
                    if pawn.cell is cell:
                        cell_canvas.create_polygon(polygon_pawn, fill=pawn.color, outline='black', width=2)