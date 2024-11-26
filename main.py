# import random
#
# from Model.Cell import Cell
# import tkinter as tk
# from tkinter import ttk, Frame
#
# from Model.Grid import Grid
#
# items_list = [
#     ("blue", "circle"),
#     ("blue", "square"),
#     ("blue", "triangle"),
#     ("blue", "star"),
#     ("red", "circle"),
#     ("red", "square"),
#     ("red", "triangle"),
#     ("red", "star"),
#     ("yellow", "circle"),
#     ("yellow", "square"),
#     ("yellow", "triangle"),
#     ("yellow", "star"),
#     ("green", "circle"),
#     ("green", "square"),
#     ("green", "triangle"),
#     ("green", "star")
# ]
#
# def create_tile(size):
#     tile = []
#     for i in range(size):
#         tile.append([])
#         for j in range(size):
#             tile[i].append(Cell(i,j))
#     tile[7][6].walls['E'] = True
#     tile[6][7].walls['S'] = True
#     return tile
#
# def build_tile_1():
#     tile = create_tile(8)
#     tile[0][3].walls['E'] = True
#     tile[1][5].walls['E'] = True
#     tile[1][6].walls['S'] = True
#     tile[2][1].walls['S'] = True
#     tile[3][1].walls['E'] = True
#     tile[3][5].walls['S'] = True
#     tile[4][4].walls['E'] = True
#     tile[5][2].walls['E'] = True
#     tile[5][2].walls['S'] = True
#     tile[5][7].walls['E'] = True
#     tile[5][7].walls['S'] = True
#     tile[6][0].walls['S'] = True
#
#     tile[1][6].item = items_list[0]
#     tile[3][1].item = items_list[10]
#     tile[4][5].item = items_list[13]
#     tile[5][2].item = items_list[7]
#
#     return tile
#
# def build_tile_2():
#     tile = create_tile(8)
#     tile[0][3].walls['E'] = True
#     tile[1][5].walls['E'] = True
#     tile[1][5].walls['S'] = True
#     tile[2][0].walls['E'] = True
#     tile[2][1].walls['S'] = True
#     tile[3][0].walls['S'] = True
#     tile[3][6].walls['S'] = True
#     tile[4][5].walls['E'] = True
#     tile[5][2].walls['S'] = True
#     tile[6][2].walls['E'] = True
#
#     tile[1][5].item = items_list[15]
#     tile[2][1].item = items_list[5]
#     tile[4][6].item = items_list[8]
#     tile[6][2].item = items_list[2]
#
#     return tile
#
# def build_tile_3():
#     tile = create_tile(8)
#
#     tile[0][3].walls['E'] = True
#     tile[1][0].walls['E'] = True
#     tile[1][1].walls['S'] = True
#     tile[1][6].walls['S'] = True
#     tile[2][6].walls['E'] = True
#     tile[4][2].walls['E'] = True
#     tile[4][2].walls['S'] = True
#     tile[4][7].walls['S'] = True
#     tile[5][0].walls['S'] = True
#     tile[5][6].walls['E'] = True
#
#     tile[1][1].item = items_list[6]
#     tile[2][6].item = items_list[12]
#     tile[4][2].item = items_list[3]
#     tile[5][7].item = items_list[9]
#
#     return tile
#
# def build_tile_4():
#     tile = create_tile(8)
#
#     tile[0][2].walls['E'] = True
#     tile[0][4].walls['S'] = True
#     tile[1][1].walls['S'] = True
#     tile[1][3].walls['E'] = True
#     tile[2][1].walls['E'] = True
#     tile[3][6].walls['E'] = True
#     tile[3][6].walls['S'] = True
#     tile[5][0].walls['S'] = True
#     tile[6][2].walls['E'] = True
#     tile[6][3].walls['S'] = True
#
#     tile[1][4].item = items_list[5]
#     tile[2][1].item = items_list[14]
#     tile[3][6].item = items_list[11]
#     tile[6][3].item = items_list[1]
#
#     return tile
#
# def rotate_tile_clockwise(tile, times):
#     print("rotate", times)
#     for _ in range(times):
#         new_tile = [[Cell(i, j) for j in range(len(tile))] for i in range(len(tile))]
#         for i in range(len(tile)):
#             for j in range(len(tile)):
#                 row, col = tile[i][j].row, tile[i][j].col
#                 walls = tile[row][col].walls
#                 new_col_index = len(tile) - 1 - i
#                 if walls['N']:
#                     new_tile[j][new_col_index].walls['E'] = True
#                 if walls['E']:
#                     new_tile[j][new_col_index].walls['S'] = True
#                 if walls['S']:
#                     new_tile[j][new_col_index].walls['W'] = True
#                 if walls['W']:
#                     new_tile[j][new_col_index].walls['N'] = True
#                 new_tile[j][new_col_index].item = tile[row][col].item
#         tile = new_tile
#     return tile
#
# def draw_grid(frame : Frame, grid : Grid):
#     print("draw_grid")
#     for i in range(len(grid.cells)):
#         for j in range(len(grid.cells)):
#             cell_frame = ttk.Frame(frame)
#             cell_frame.grid(row=i, column=j)
#
#             cell_canvas = tk.Canvas(cell_frame, width=50, height=50, bg='white', highlightthickness=0)
#             cell_canvas.pack(fill="both", expand = True)
#             cell_canvas.create_rectangle(0,0,50,50, width=0.1)
#
#             text = grid.cells[i][j].row, grid.cells[i][j].col
#             # print(text)
#             def print_test(event, text=text):
#                 print(text)
#
#             cell_canvas.bind('<Button-1>', print_test)
#
#             walls = grid.cells[i][j].walls
#             if walls['N']:
#                 cell_canvas.create_line(0,0,50,0,width=5)
#             if walls['E']:
#                 cell_canvas.create_line(50,0,50,50,width=5)
#             if walls['S']:
#                 cell_canvas.create_line(0,50,50,50,width=5)
#             if walls['W']:
#                 cell_canvas.create_line(0,0,0,50,width=5)
#
#             item = grid.cells[i][j].item
#             if item != (None,None):
#                 color = item[0]
#                 match(item[1]):
#                     case "circle":
#                         cell_canvas.create_oval(10,10,40,40,fill=color)
#                     case "square":
#                         cell_canvas.create_rectangle(10,10,40,40, fill=color)
#                     case "triangle":
#                         cell_canvas.create_polygon([25,10,10,40,40,40], fill=color)
#                     case "star":
#                         cell_canvas.create_oval(10,15,40,30, fill=color)
#
#
#
# def test_button():
#     print("okay lezgo")
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title("Rasende Roboter")
#     main_frame = ttk.Frame(root, padding="10")
#     main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#
#     # Create grid frame
#     grid_frame = ttk.Frame(main_frame)
#     grid_frame.grid(row=0, column=0, padx=5, pady=5)
#
#     # Create buttons frame
#     buttons_frame = ttk.Frame(main_frame)
#     buttons_frame.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)
#
#     tiles = [build_tile_1(),build_tile_2(),build_tile_3(),build_tile_4()]
#
#     random.shuffle(tiles)
#
#     for i in range(1,4):
#         tiles[i] = rotate_tile_clockwise(tiles[i], i)
#
#     grid = Grid(tiles[0],tiles[1],tiles[2],tiles[3])
#     draw_grid(grid_frame, grid)
#
#
#     button_test = ttk.Button(buttons_frame, text="Test", command=test_button)
#     button_test.grid(row=0, column=0)  # Add the button to the grid
#
#     root.mainloop()

import tkinter as tk

from Controller.Controller import Controller

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Rasende Roboter")
    app = Controller(root)
    root.mainloop()