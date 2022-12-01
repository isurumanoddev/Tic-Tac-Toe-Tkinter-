from tkinter import *
from tkinter import messagebox

window = Tk()
frame = Frame(window)
frame.pack()

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
clicked = True


def emapty_space():
    spaces = 9

    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] != "":
                spaces -= 1

    if spaces == 0:
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(background="red")
        return False


def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return 1
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            return 1
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return 1
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return 1
    elif emapty_space() == False:
        return "tie"
    else:
        return 0


def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=DISABLED)


def new_game():
    global buttons
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=("consalas", 25), background="light green", height=3, width=6,
                                          activebackground="brown",
                                          command=lambda row=row, column=column: button_click(row, column))
            buttons[row][column].grid(row=row, column=column)


new_game()


def button_click(row, column):
    global clicked
    if buttons[row][column]["text"] == "" and clicked == True:
        buttons[row][column].config(text="X", background="Yellow")
        label.config(text=" It's O Turn ")
        clicked = False
        if check_winner() == 1:
            disable_buttons()
            messagebox.showinfo("You won the game", "play again")
        elif check_winner() == "tie":
            disable_buttons()
            label.config(text=" It's Tie ,Match drawn ")


    elif buttons[row][column]["text"] == "" and clicked == False:
        buttons[row][column].config(text="O", background="white")
        label.config(text=" It's X Turn ")
        clicked = True
        if check_winner() == 1:
            disable_buttons()
            messagebox.showinfo("You won the game", "play again")
        elif check_winner() == "tie":
            disable_buttons()
            label.config(text=" It's Tie ,Match drawn ")


label = Label(window, font=("consalas", 25), text=" It's X Turn ")
label.pack()
reset_button = Button(window, font=("consalas", 25), text="New Game", command=new_game)
reset_button.pack()

window.mainloop()
