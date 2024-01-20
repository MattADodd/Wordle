from tkinter import *
import requests as rq
import random

# Fetch a list of words from a URL and split them into a list
words = rq.get('https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/c915fa3264be6d35990d0edb8bf927df7a015602/wordle-answers-alphabetical.txt')
word_list = words.text.split('\n')

# Choose a random word from the list and convert it to uppercase
random_number = random.randint(0, 2315)
solution = word_list[random_number].upper()

# Counter to keep track of attempts, starting with the first attempt
counter = 1

# List of entry names and corresponding dictionary for indexing
entry_list = ['first_entry', 'second_entry', 'third_entry', 'fourth_entry', 'fifth_entry']
entry_dict = {'first_entry': 0, 'second_entry': 1, 'third_entry': 2, 'fourth_entry': 3, 'fifth_entry': 4}

# String to store the current attempt word
word = ''

# Create the main Tkinter window
root = Tk()
root.title('Homemade Wordle')

# Function to handle button press for letter selection
def button_press(letter):
    # Check each entry and fill the first empty one with the selected letter
    for entry in entry_list:
        if globals()[entry + str(counter)]['text'] == '':
            globals()[entry + str(counter)]['text'] = letter
            break

# Function to handle button press for delete
def delete_button():
    # Delete the last filled entry, if any
    for entry in reversed(entry_list):
        if globals()[entry + str(counter)]['text'] != '':
            globals()[entry + str(counter)]['text'] = ''
            break
    submit.config(state=DISABLED)

# Function to handle button press for submit
def submit_button():
    global word, counter
    
    # Check each entry against the solution and update the display accordingly
    for entry in entry_list:
        if globals()[entry + str(counter)]['text'] == solution[entry_dict[entry]]:
            globals()[entry + str(counter)].config(bg='green')
            word = word + globals()[entry + str(counter)]['text']

    # Check each entry for correct letters in the wrong position and update the display
    for entry in entry_list:
        word = word + globals()[entry + str(counter)]['text']
        if globals()[entry + str(counter)]['text'] in solution and word.count(word[-1]) <= solution.count(word[-1]):
            globals()[entry + str(counter)].config(bg='orange')
    
    submit.config(state=DISABLED)

    # Check if the current attempt matches the solution and show a popup if so
    if globals()['first_entry' + str(counter)]['text'] + globals()['second_entry' + str(counter)]['text'] + globals()['third_entry' + str(counter)]['text'] + globals()['fourth_entry' + str(counter)]['text'] + globals()['fifth_entry' + str(counter)]['text'] == solution:
        win_popup()
    
    counter += 1

    # Check if the maximum number of attempts is reached and show a popup if so
    if counter == 7:
        lose_popup()

    word = ''  # Reset the word for the next attempt

# Popup for winning the game
def win_popup():
    top = Toplevel(win)
    top.geometry('100x30')
    top.title('WINNER')
    Label(top, text='YOU WIN!!', font=500).pack()
    for widget in root.winfo_children():
        if widget.winfo_class() == 'Button':
            widget.config(state=DISABLED)

# Popup for losing the game
def lose_popup():
    top = Toplevel(win)
    top.geometry('100x30')
    top.title('Loser')
    Label(top, text='YOU LOSE', font=500).pack()
    for widget in root.winfo_children():
        if widget.winfo_class() == 'Button':
            widget.config(state=DISABLED)

# Creating Labels for entries in the GUI
for i in range(1, 7):
    for j, entry in enumerate(entry_list, start=1):
        globals()[f'{entry}{i}'] = Label(text='', width=5, height=5, fg='white', bg='black')
        globals()[f'{entry}{i}'].grid(row=10*i, column=j, padx=10, pady=10)

# Creating Buttons for letter selection in the GUI
for i, letter in enumerate('ABCDEFGHIJKLM', start=0):
    button = Button(root, text=letter, width=1, height=1, command=lambda l=letter: button_press(l))
    button.grid(row=60, column=i)

# Creating Buttons for letter selection in the GUI
for i, letter in enumerate('NOPQRSTUVWXYZ', start=0):
    button = Button(root, text=letter, width=1, height=1, command=lambda l=letter: button_press(l))
    button.grid(row=65, column=i)

# Create additional buttons for V-Z, delete, and submit
letters = ['V', 'W', 'X', 'Y', 'Z', 'Del', 'Enter']
commands = [lambda l=letter: button_press(l) for letter in letters[:-2]] + [delete_button, submit_button]
for i, (letter, command) in enumerate(zip(letters, commands), start=0):
    button = Button(root, text=letter, width=3 if letter == 'Enter' else 2, height=1, command=command, state=DISABLED if letter == 'Enter' else NORMAL)
    button.grid(row=70, column=i)

# Label to display win/lose message
win = Label(text='YOU WIN!!')

# Start the Tkinter main loop
root.mainloop()
