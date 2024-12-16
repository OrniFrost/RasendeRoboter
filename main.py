import tkinter as tk
from Controller.BoardController import BoardController
from Controller.GameController import GameController
from Controller.PlayerController import PlayerController
from Controller.AIController import AIController

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Rasende Roboter")

    board_controller = BoardController(root)
    view = board_controller.view
    player_controller = PlayerController(root,board_controller.grid, view)
    ai_controller = AIController(root,board_controller.grid, view)

    game_controller = GameController(root,board_controller.grid,view,player_controller,ai_controller)

    root.mainloop()