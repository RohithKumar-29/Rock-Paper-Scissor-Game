import tkinter as tk
import random

def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissor")
heading = tk.Label(root, text="ROCK, PAPER AND SCISSOR GAME", font=('verdana', 50), fg='darkblue')
heading.pack(pady=20)

rock_button = tk.Button(root, text="Rock",font=('verdana',25), width=25, command=lambda: play('Rock'))
paper_button = tk.Button(root, text="Paper",font=('verdana',25), width=25, command=lambda: play('Paper'))
scissors_button = tk.Button(root, text="Scissors",font=('verdana',25), width=25, command=lambda: play('Scissors'))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", font=('verdana', 50),fg= 'green', pady=10)
result_label.pack()

root.mainloop()
