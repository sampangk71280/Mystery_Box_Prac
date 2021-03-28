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
        print(stakes)
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()
        # Set starting balance to amount entered by user of game
        self.balance.set(starting_balance)

        # get value of stakes (use it as a multiplier when calculating winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # List for holding statistics
        self.round_stats_list = []

        # GUI Setup
        self.game_box = Toplevel()

        # If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

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

        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="Mystery_box_images/question.gif")

        self.prize1_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize1_label.photo= photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.reveal_boxes)

        # bind button to <enter> (users can push enter to reveal the boxes)
        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
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
                                  bg="#808080", fg="white", command=self.help)
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Game Stats...",
                                   font="Arial 15 bold", bg="#006633", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)


    def reveal_boxes(self):
        # retrieval the balance from the initial function..
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []
        for item in range(0, 3):
            prize_num = random.randint (1,100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file="Mystery_box_images/gold_med.gif")
                prize_list = "gold (${})".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize = PhotoImage(file="Mystery_box_images/silver_med.gif")
                prize_list = "silver (${})".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = PhotoImage(file="Mystery_box_images/copper_med.gif")
                prize_list = "copper (${})".format(1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
            else:
                prize = PhotoImage(file="Mystery_box_images/lead.gif")
                prize_list = "lead\n($0)"

            prizes.append(prize)
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # Display prizes...
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo=photo1
        self.prize2_label.config(image=photo2)
        self.prize2_label.photo=photo2
        self.prize3_label.config(image=photo3)
        self.prize3_label.photo=photo3

        # deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # add winnings
        current_balance += round_winnings

        # set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}\n Payback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings, current_balance)

        # add round results to statistics list
        round_summary = "{} | {} | {} - Cost: ${} | " \
                        "Payback: ${} | Current Balance: " \
                        "${}".format(stats_prizes[0], stats_prizes[1],
                                     stats_prizes[2],
                                     5 * stakes_multiplier, round_winnings,
                                     current_balance)
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)

        # edit label so user can see their balance
        self.balance_label.config(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\n" \
                                "Your balance is too low. You can only quit " \
                                "or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                      text=balance_statement)
    def to_quit(self):
        root.destroy()

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Choose an amount to play with and then choose "
                                          "the stakes. Higher stakes cost more per round "
                                          "but you can win more as well. \n\n"
                                          "When you enter the play area, you will see "
                                          "three mystery boxes. To reveal the "
                                          "contents of the boxes, click the 'Open Boxes' "
                                          "button. If you don't have enough money to play, "
                                          "the button will turn red and you need to quit "
                                          "the game. \n\n"
                                          "The contents of the boxes will be added to your "
                                          "Balance. The boxes could contain\n\n"
                                          "Low: Lead ($0) | Copper ($1) | Silver ($2) | Gold ($10)\n"
                                          "Medium: Lead ($0) | Copper ($2) | Silver ($4) | Gold ($25)\n"
                                          "High: Lead ($0) | Copper ($5) | Silver ($10) | Gold ($50)\n\n"
                                          "If each box contains gold, you earn $30 (lowstakes). If "
                                          "they contained copper, silver, and gold, you would receive "
                                          "$13 ($1 - $2 - $10) and so on.",
                                     padx=10)

class Help:
    def __init__(self, partner):



        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Rules",
                                 font="arial 10 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, wrap=250)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="#C20000",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Boxes")
    something = Start(root)
    root.mainloop()
