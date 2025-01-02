import tkinter as tk
from Controller.BoardController import BoardController
from Controller.GameController import GameController
from Controller.PlayerController import PlayerController
from Controller.AIController import AIController

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Rasende Roboter")

    is_random_board = True

    board_controller = BoardController(root, is_random_board)
    view = board_controller.view
    ai_controller = AIController(root,board_controller.grid, view)
    player_controller = PlayerController(root,board_controller.grid, view)

    game_controller = GameController(root,board_controller.grid,view,player_controller,ai_controller)

    root.mainloop()