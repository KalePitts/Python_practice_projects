import tkinter as tk

root = tk.Tk()

root.geometry("1000x800")
root.title("Shapes")

def choose_rock():
    label.configure(text = "You chose rock!")

def choose_paper():
    label.configure(text = "You chose paper!")
    
def choose_scissors():
    label.configure(text = "You chose scissors!")

label = tk.Label(root, text="Hello World!", font = ('Comic Sans', 18))
label.pack()

choice_frame = tk.Frame(root, padx = 2, pady= 8)
choice_frame.pack(expand = True, fill = 'x')

button_rock = tk.Button(choice_frame, text = "Rock", command = choose_rock,height=7)
button_paper = tk.Button(choice_frame, text = "Paper", command = choose_paper,height=7)
button_scissors = tk.Button(choice_frame, text = "Scissors", command = choose_scissors,height=7)

button_decide = tk.Button(root, text = "Submit")

button_rock.pack(expand=True,side="left",fill='x')
button_paper.pack(expand=True,side="left",fill='x')
button_scissors.pack(expand=True,side="left",fill='x')

button_decide.pack()

root.mainloop()