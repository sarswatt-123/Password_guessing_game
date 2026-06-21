import tkinter as tk
import random

jackpot = random.randint(1, 100)
counter = 0

def check_guess():
    global counter
    
    guess = int(entry.get())
    counter += 1
    
    if guess < jackpot:
        result.config(text="Your guess is too low")
    elif guess > jackpot:
        result.config(text="Your guess is too high")
    else:
        result.config(text=f"Correct! You guessed in {counter} attempts")


# Window create
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

# Heading
heading = tk.Label(root, text="Guess Number (1-100)")
heading.pack(pady=10)

# Input box
entry = tk.Entry(root)
entry.pack()

# Button
button = tk.Button(root, text="Check", command=check_guess)
button.pack(pady=10)

# Result label
result = tk.Label(root, text="")
result.pack()

# Run window
root.mainloop()