import tkinter as tk
from Controller.BoardController import BoardController
from Controller.PlayerController import PlayerController
from Controller.AIController import AIController

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Rasende Roboter")

    board_controller = BoardController(root)
    view = board_controller.view
    player_controller = PlayerController(board_controller.grid, view)
    ai_controller = AIController(board_controller.grid, view)

    root.mainloop()