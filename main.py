import tkinter as tk
from Controller.BoardController import BoardController
from Controller.PlayerController import PlayerController

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Rasende Roboter")

    board_controller = BoardController()
    player_controller = PlayerController(root, board_controller.grid)

    root.mainloop()