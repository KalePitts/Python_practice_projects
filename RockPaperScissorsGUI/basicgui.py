import tkinter as tk
import random

root = tk.Tk()
root.geometry("1000x800")
root.title("Rock Paper Scissors")
random.seed()

def battle(player_choice,opponent_choice):
    global wins, losses
    if player_choice == opponent_choice:
        open_result_window("You both chose the same fighter! It's a draw!")
    elif player_choice == "rock":
        if opponent_choice == "paper":
            open_result_window("Your rock vs. their paper! You lose!")
            losses +=1
        else:
            open_result_window("Your rock vs. their scissors! You win!")
            wins +=1
    elif player_choice == "paper":
        if opponent_choice == "scissors":
            open_result_window("Your paper vs. their scissors! You lose!")
            losses +=1
        else:
            open_result_window("Your paper vs. their rock! You win!")
            wins +=1
    elif player_choice == "scissors":
        if opponent_choice == "rock":
            open_result_window("Your scissors vs. their rock! You lose!")
            losses +=1
        else:
            open_result_window("Your scissors vs their paper! You win!")
            wins +=1
    update_main_window()

def submit_answer():
    global prospective_choice
    if(prospective_choice != "none"):
        final_choice = prospective_choice
        prospective_choice = "none"
        opponent_choice = random.choice(["rock","paper","scissors"])
        battle(final_choice, opponent_choice)
    else:
        open_result_window("You did not choose a fighter! Try again.")

def update_main_window():
    global wins,losses
    selection_label.configure(text = "Select your fighter!")
    opponent_label.configure(text = "Your opponent awaits your decision.")
    photo_label.configure(image = selection_image)
    win_label.configure(text = "Your wins: " + str(wins))
    lose_label.configure(text = "Your losses: " + str(losses))


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

def open_result_window(result_str):
    new_window = tk.Toplevel(root)
    new_window.geometry("500x400")
    new_window.focus_force()
    result_label = tk.Label(new_window, text = result_str, font = ('Comic Sans', 15), pady= 150).pack()

global prospective_choice
prospective_choice = "none"
global wins 
wins = 0
global losses
losses = 0

choice_frame = tk.Frame(root, padx = 40,pady=20)
counter_frame = tk.Frame(root,padx = 40,pady=10)

selection_label = tk.Label(root, text="Select your fighter!", font = ('Comic Sans', 18),pady=20)
opponent_label = tk.Label(root, text = "Your opponent awaits your decision.", font = ('Comic Sans', 24),pady=100)
win_label = tk.Label(counter_frame, text = "Your wins: " + str(wins), font = ('Comic Sans', 12))
lose_label = tk.Label(counter_frame, text = "Your losses: " + str(losses), font = ('Comc Sans',12))

button_rock = tk.Button(choice_frame, text = "Rock", command = choose_rock,height=7)
button_paper = tk.Button(choice_frame, text = "Paper", command = choose_paper,height=7)
button_scissors = tk.Button(choice_frame, text = "Scissors", command = choose_scissors,height=7)
button_decide = tk.Button(root, text = "Battle!", command = submit_answer)

selection_image = tk.PhotoImage(file = "images/selection.png")
photo_label = tk.Label(image=selection_image)
rock_image = tk.PhotoImage(file = "images/rock.png")
paper_image = tk.PhotoImage(file = "images/paper.png")
scissors_image = tk.PhotoImage(file = "images/scissors.png")

counter_frame.pack(fill = 'x')
win_label.pack(side="left")
lose_label.pack(side="right")
selection_label.pack()
photo_label.pack()
choice_frame.pack(fill = 'x')
button_rock.pack(expand=True,side="left",fill='x')
button_paper.pack(expand=True,side="left",fill='x')
button_scissors.pack(expand=True,side="left",fill='x')
button_decide.pack()
opponent_label.pack()

root.mainloop()