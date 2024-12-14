import tkinter as tk
from tkinter import simpledialog, ttk

from Controller.AIController import AIController
from Controller.PlayerController import PlayerController
from View.GridView import GridView


class GameController:

    def __init__(self,root,
                 grid : GridView,
                 player_controller : PlayerController,
                 ai_controller : AIController
                 ):
        self.root = root
        self.grid = grid
        self.player_controller = player_controller
        self.ai_controller = ai_controller

        self.pop_menu = tk.Menu(self.root)
        self.ask_for_settings()



    def ask_for_settings(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Game Settings")

        ttk.Label(dialog, text="AI Level:").grid(row=0, column=0, padx=10, pady=10)
        ai_level_combobox = ttk.Combobox(dialog, values=["easy", "medium", "hard"])
        ai_level_combobox.grid(row=0, column=1, padx=10, pady=10)
        ai_level_combobox.current(0)  # Set default value

        ttk.Label(dialog, text="Number of Rounds:").grid(row=1, column=0, padx=10, pady=10)
        rounds_var = tk.IntVar(value=3)  # Default value

        round_options = [3, 5, 7]
        for idx, val in enumerate(round_options):
            tk.Radiobutton(dialog, text=str(val), variable=rounds_var, value=val).grid(row=1, column=idx + 1, padx=5,
                                                                                       pady=10)

        def on_submit():
            ai_level = ai_level_combobox.get()
            num_rounds = rounds_var.get()
            if ai_level:
                print(f"AI Level: {ai_level}, Number of Rounds: {num_rounds}")
                dialog.destroy()
            else:
                print("Invalid input")

        submit_button = ttk.Button(dialog, text="Submit", command=on_submit)
        submit_button.grid(row=2, column=0, columnspan=4, pady=10)

        dialog.transient(self.root)
        dialog.grab_set()
        self.root.wait_window(dialog)