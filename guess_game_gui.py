import tkinter as tk
import random

def start_game():
    global low, high, num, chances, attempts

    output.delete("1.0", tk.END)

    try:
        low = int(lower_entry.get())
        high = int(upper_entry.get())
    except:
        output.insert(tk.END, "Please enter valid numbers!\n")
        return

    if low >= high:
        output.insert(tk.END, "Lower bound must be smaller than upper bound!\n")
        return

    num = random.randint(low, high)
    chances = 7
    attempts = 0

    output.insert(tk.END, f"Game started!\nGuess a number between {low} and {high}.\n")
    output.insert(tk.END, f"You have {chances} chances.\n\n")


def check_guess():
    global attempts

    if attempts >= chances:
        output.insert(tk.END, f"No more chances! The number was {num}.\n")
        return

    try:
        guess = int(guess_entry.get())
    except:
        output.insert(tk.END, "Enter a valid number.\n")
        return

    attempts += 1

    # إظهار الرقم اللي كتبه المستخدم
    output.insert(tk.END, f"You entered: {guess}\n")

    guess_entry.delete(0, tk.END)

    if guess == num:
        output.insert(tk.END, f"Correct! You guessed it in {attempts} attempts.\n")
    elif attempts >= chances:
        output.insert(tk.END, f"Sorry! You're out of chances.\nThe number was {num}.\n")
    elif guess > num:
        output.insert(tk.END, "Too high! Try lower.\n\n")
    else:
        output.insert(tk.END, "Too low! Try higher.\n\n")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x500")

tk.Label(root, text="Lower Bound:").pack()
lower_entry = tk.Entry(root)
lower_entry.pack()

tk.Label(root, text="Upper Bound:").pack()
upper_entry = tk.Entry(root)
upper_entry.pack()

tk.Button(root, text="Start Game", command=start_game).pack(pady=10)

tk.Label(root, text="Enter your guess:").pack()
guess_entry = tk.Entry(root)
guess_entry.pack()

tk.Button(root, text="Submit Guess", command=check_guess).pack(pady=10)

output = tk.Text(root, height=15, width=50)
output.pack(pady=10)

root.mainloop()
