from tkinter import *
from functools import partial # to prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        # GUI To get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()


        self.push_me_button = Button(self.start_frame, text="Push Now",
                                     command=self.to_game)
        self.push_me_button.grid(row=0)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 2

        self.start_frame.destroy()
        Game(self, stakes, starting_balance)

class Game:
    def __init__(self, partner, stakes, starting_balance):

        # Formatting variables...
        self.game_stats_list=[50,6]

        self.round_stats_list=['copper ($3) | copper ($3) | lead($0) - Cost: $15 | Payback: $6 | Current Balance: $41', 'copper ($3) | copper ($3) | lead($0) - Cost: $15 | Payback: $6 | Current Balance: $32', 'copper ($3) | lead($0) | copper ($3) - Cost: $15 | Payback: $6 | Current Balance: $23', 'copper ($3) | silver ($6) | lead($0) - Cost: $15 | Payback: $9 | Current Balance: $17', 'lead($0) | silver ($6) | copper ($3) - Cost: $15 | Payback: $9 | Current Balance: $11']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Stats Button (row 1)
        self.stats_button = Button(self.game_frame, text="Game Stats",
                                   font="Arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

class GameStats:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Game Statistics. "
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Starting Balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Starting Balance (row 2.0)

        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance: ", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                         text="${}".format(game_stats[0]),
                                               anchor="w")
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # current balance (row2.2)
        self.current_balance_label = Label(self.details_frame,
                                           text="Current Balance:", font=heading,
                                           anchor="e")
        self.current_balance_label.grid(row=1, coloumn=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                  text="${}".format(game_stats[1]), anchor="e")
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg="green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost (row 2.3)
        self.win_loss_label= Label(self.details_frame, text=win_loss,
                                   font=heading, anchor="e")
        self.win_loss_label.grid(row=2, column=0, padx=0)

        self.win_loss_value_label = Label(self.details_frame, font=content,
                                          text="${}".format(amount),
                                          fg=win_loss_fg, anchor="w")
        self.win_loss_value_label.grid(row=2, column=1, padx=0)

        # Rounds Played (row 2.4)
        self.games_played_label=Label(self.details_frame, text="Rounds Played:",
                                      font=heading, anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=content,
                                              text=len(game_history), anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

    def close_stats(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Boxes")
    something = Start(root)
    root.mainloop()
