import tkinter as tk
import random

root = tk.Tk()
root.geometry("1000x800")
root.title("Rock Paper Scissors")
random.seed()

def battle(player_choice,opponent_choice):
    if player_choice == opponent_choice:
        selection_label.configure(text = "It's a draw!")
        return
    if player_choice == "rock":
        if opponent_choice == "paper":
            selection_label.configure(text = "You lost!")
        else:
            selection_label.configure(text = "You won!")
    elif player_choice == "paper":
        if opponent_choice == "scissors":
            selection_label.configure(text = "You lost!")
        else:
            selection_label.configure(text = "You won!")
    elif player_choice == "scissors":
        if opponent_choice == "rock":
            selection_label.configure(text = "You lost!")
        else:
            selection_label.configure(text = "You won!")

def submit_answer():
    if(prospective_choice != "none"):
        final_choice = prospective_choice
        opponent_choice = random.choice(["rock","paper","scissors"])
        opponent_label.configure(text = "The opponent chose " + opponent_choice + "!")
        battle(final_choice, opponent_choice)

def choose_rock():
    selection_label.configure(text = "You choose rock!")
    photo_label.configure(image = rock_image)
    global prospective_choice
    prospective_choice = "rock"

def choose_paper():
    selection_label.configure(text = "You choose paper!")
    photo_label.configure(image = paper_image)
    global prospective_choice 
    prospective_choice = "paper"
    
def choose_scissors():
    selection_label.configure(text = "You choose scissors!")
    photo_label.configure(image = scissors_image)
    global prospective_choice 
    prospective_choice = "scissors"

selection_label = tk.Label(root, text="Select your fighter!", font = ('Comic Sans', 18),pady=20)
opponent_label = tk.Label(root, text = "Your opponent awaits your decision.", font = ('Comic Sans', 24),pady=100)

choice_frame = tk.Frame(root, padx = 2,pady=20)

button_rock = tk.Button(choice_frame, text = "Rock", command = choose_rock,height=7)
button_paper = tk.Button(choice_frame, text = "Paper", command = choose_paper,height=7)
button_scissors = tk.Button(choice_frame, text = "Scissors", command = choose_scissors,height=7)
button_decide = tk.Button(root, text = "Battle!", command = submit_answer)

selection_image = tk.PhotoImage(file = "images/selection.png")
photo_label = tk.Label(image=selection_image)
rock_image = tk.PhotoImage(file = "images/rock.png")
paper_image = tk.PhotoImage(file = "images/paper.png")
scissors_image = tk.PhotoImage(file = "images/scissors.png")


selection_label.pack()
photo_label.pack()
choice_frame.pack(fill = 'x')
button_rock.pack(expand=True,side="left",fill='x')
button_paper.pack(expand=True,side="left",fill='x')
button_scissors.pack(expand=True,side="left",fill='x')
button_decide.pack()
opponent_label.pack()



root.mainloop()