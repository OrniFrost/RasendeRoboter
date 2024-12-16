import tkinter as tk
import random
from tkinter import simpledialog, ttk, StringVar

from Controller.AIController import AIController
from Controller.PlayerController import PlayerController
from Model.Cell import Cell
from Model.Grid import Grid
from Model.Pawn import Pawn
from View.GridView import GridView

from constants import items_list, ai_levels

class GameController:

    def __init__(self, root : tk.Tk,
                 grid : Grid,
                 view : GridView,
                 player_controller : PlayerController,
                 ai_controller : AIController
                 ):
        self.root = root
        self.grid = grid
        self.view = view
        self.player_controller = player_controller
        self.ai_controller = ai_controller


        self.remaining_items_list = items_list.copy()

        self.ai_level: str = ""
        self.number_of_rounds: int = 0

        self.pop_menu = tk.Menu(self.root)
        self.ask_for_settings()

        print(self.ai_level, self.number_of_rounds)

        self.do_the_game()

    def ask_for_settings(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Game Settings")

        ttk.Label(dialog, text="AI Level:").grid(row=0, column=0, padx=10, pady=10)
        ai_level_combobox = ttk.Combobox(dialog, values=ai_levels)
        ai_level_combobox.grid(row=0, column=1, padx=10, pady=10)
        ai_level_combobox.current(0)  # Set default value

        ttk.Label(dialog, text="Number of Rounds:").grid(row=1, column=0, padx=10, pady=10)
        rounds_var = tk.IntVar(value=3)  # Default value

        round_options = [3, 5, 7]
        for idx, val in enumerate(round_options):
            tk.Radiobutton(dialog, text=str(val), variable=rounds_var, value=val).grid(row=1, column=idx + 1, padx=5,
                                                                                       pady=10)

        def on_submit():
            self.ai_level = ai_level_combobox.get()
            self.number_of_rounds = rounds_var.get()
            dialog.destroy()

        submit_button = ttk.Button(dialog, text="Submit", command=on_submit)
        submit_button.grid(row=2, column=0, columnspan=4, pady=10)

        dialog.transient(self.root)
        dialog.grab_set()
        self.root.wait_window(dialog)


    def do_the_game(self):
        for i in range(1, self.number_of_rounds+1):
            #Tirer une cible
            target = self.choose_target()
            self.view.actualize_round(i, target)

            #IA play
            self.ai_controller.make_turn(target)


            # Player
            # self.player_controller.is_playing = True
            # while self.player_controller.is_playing:
            #     self.player_controller.make_turn(target)
            # self.player_controller.is_playing.set(True)
            self.player_controller.make_turn(target)

            print(f"AI : {self.ai_controller.moves_counter} - Player : {self.player_controller.moves_counter}")
            if self.ai_controller.moves_counter >= self.player_controller.moves_counter :
                self.player_controller.rounds_won += 1
            else:
                self.ai_controller.rounds_won += 1

            self.view.update_scores(ai_score=self.ai_controller.rounds_won,
                                    player_score=self.player_controller.rounds_won)

            # Reset counters
            self.ai_controller.reset_moves_counter()
            self.player_controller.reset_moves_counter()

        #End of the game
        if self.ai_controller.rounds_won > self.player_controller.rounds_won :
            print("Player wins")
        else:
            print("AI wins")

        self.root.quit()

    def choose_target(self):
        is_okay = False
        while not is_okay:
            target = random.choice(self.remaining_items_list)
            color_target = target[0]
            for pawn in self.grid.pawns:
                if color_target == pawn.color:
                    pawn_of_the_target: Pawn = pawn

            cell_of_the_target = self.grid.find_cell_of_target(target)

            # print(cell_of_the_target)

            cells_not_valid : [Cell] = self.player_controller.find_possibles_moves(pawn_of_the_target)
            cells_not_valid.append(cell_of_the_target)

            if pawn_of_the_target.cell not in cells_not_valid:
                is_okay = True
            else :
                is_okay = False

        self.remaining_items_list.remove(target)
        return target