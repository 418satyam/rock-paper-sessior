import random
import tkinter as tk

choices = ["Rock", "Paper", "Scissors"]
me = 0
opponent = 0

def choice(my_choice, opponent_choice):
    if my_choice == opponent_choice:
        return "It's a Tie!"
    elif (my_choice == "Rock" and opponent_choice == "Scissors") or \
         (my_choice == "Scissors" and opponent_choice == "Paper") or \
         (my_choice == "Paper" and opponent_choice == "Rock"):
        return "You Win!"
    else:
        return "You Lose!"

def start(my_choice):
    global me, opponent
    opponent_choice = random.choice(choices)
    result = choice(my_choice, opponent_choice)

    if result == "You Win!":
        me += 1
    elif result == "You Lose!":
        opponent += 1

    result_label.config(
        text="me chose: " + my_choice + "\n opponent chose: " + opponent_choice + "\n" + result
    )
    score_label.config(
        text="Score - opponent: " + str(me) + " | opponent: " + str(opponent)
    )

def restart():
    global me, opponent
    me = 0
    opponent = 0
    result_label.config(text="")
    score_label.config(text="Score - me: 0 | opponent: 0")

0
rsp = tk.Tk()
rsp.title("Rock Paper Scissors")
rsp.geometry("500x400")
rsp.config(bg="white")

title_label = tk.Label(rsp, text="Rock - Paper - Scissors", font=("Arial", 20, "bold"), bg="white")
title_label.pack(pady=10)

button_frame = tk.Frame(rsp, bg="white")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: start("Rock"))
paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: start("Paper"))
scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: start("Scissors"))

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(rsp, text="", font=("Arial", 14), bg="white", fg="black")
score_label = tk.Label(rsp, text="Score - me: 0 | opponent: 0", font=("Arial", 12), bg="white", fg="black")
restart_button = tk.Button(rsp, text="Restart Game", font=("Arial", 12), command=restart, bg="lightgray")

result_label.pack(pady=20)
score_label.pack(pady=10)
restart_button.pack(pady=15)

rsp.mainloop()
