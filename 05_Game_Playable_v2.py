from tkinter import *
from functools import partial # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI To get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()


        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 2

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()



class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()
        # Set starting balance to amount entered by user of game
        self.balance.set(starting_balance)

        # get value of stakes (use it as a multiplier when calculating winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row (row 0)
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open "
                                             "Boxes' button to reveal the "
                                             "contents of the mystery boxes.",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back = "#b6ea96" # light green
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)


        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                               bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2)

        # play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # Balance Label (row 4)

        start_text = "Game Cost: ${} \n ""\n How much " \
                     "will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="Arial  12 bold", fg="green",
                                   text=start_text, wrap=300, justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

    def reveal_boxes(self):
        # retrieval the balance from the initial function..
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        backgrounds = []
        for item in range(0, 3):
            prize_num = random.randint (1,100)

            if 0 < prize_num <= 5:
                prize = "gold\n(${})".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
                back_colour = "#CEA935" # Gold colours
            elif 5 < prize_num <= 25:
                prize = "silver\n(${})".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
                back_colour = "#B7B7B5" # Silver colour
            elif 25 < prize_num <= 65:
                prize = "copper\n(${})".format(1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
                back_colour = "#BC7F61" # copper colour
            else:
                prize = "lead\n($0)"

            prizes.append(prize)
            backgrounds.append(back_colour)

        # Display prizes...
        self.prize1_label.config(text=prizes[0], bg)
        self.prize2_label.config(text=prizes[1])
        self.prize3_label.config(text=prizes[2])

        # deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # add winnings
        current_balance += round_winnings

        # set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}\n Payback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings, current_balance)

        # edit label so user can see their balance
        self.balance_label.config(text=balance_statement)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Boxes")
    something = Start(root)
    root.mainloop()
