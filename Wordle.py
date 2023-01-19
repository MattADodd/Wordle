from tkinter import *
import requests as rq
import random

words = rq.get('https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/c915fa3264be6d35990d0edb8bf927df7a015602/wordle-answers-alphabetical.txt')
word_list = words.text.split('\n')
random_number = random.randint(0, 2315)
solution = word_list[random_number].upper()
counter = 1
entry_list = ['first_entry', 'second_entry', 'third_entry', 'fourth_entry', 'fifth_entry']
entry_dict = {'first_entry': 0, 'second_entry': 1, 'third_entry': 2, 'fourth_entry': 3, 'fifth_entry': 4}
word = ''
root = Tk()
root.title('Homemade Wordle')

def button_press(letter):
    if globals()['first_entry' + str(counter)]['text'] == '':
        globals()['first_entry' + str(counter)]['text'] = letter
    elif globals()['second_entry' + str(counter)]['text'] == '':
        globals()['second_entry' + str(counter)]['text'] = letter
    elif globals()['third_entry' + str(counter)]['text'] == '':
        globals()['third_entry' + str(counter)]['text'] = letter
    elif globals()['fourth_entry' + str(counter)]['text'] == '':
        globals()['fourth_entry' + str(counter)]['text'] = letter
    elif globals()['fifth_entry' + str(counter)]['text'] == '':
        globals()['fifth_entry' + str(counter)]['text'] = letter
        submit.config(state=NORMAL)

def delete_button():
    if globals()['fifth_entry' + str(counter)]['text'] != '':
        globals()['fifth_entry' + str(counter)]['text'] = ''
    elif globals()['fourth_entry' + str(counter)]['text'] != '':
        globals()['fourth_entry' + str(counter)]['text'] = ''
    elif globals()['third_entry' + str(counter)]['text'] != '':
        globals()['third_entry' + str(counter)]['text'] = ''
    elif globals()['second_entry' + str(counter)]['text'] != '':
        globals()['second_entry' + str(counter)]['text'] = ''
    elif globals()['first_entry' + str(counter)]['text'] != '':
        globals()['first_entry' + str(counter)]['text'] = ''
    submit.config(state=DISABLED)

def submit_button():
    global word
    global counter
    for entry in entry_list:
        if globals()[entry + str(counter)]['text'] == solution[entry_dict[entry]]:
            globals()[entry + str(counter)].config(bg='green')
            word = word + globals()[entry + str(counter)]['text']
    for entry in entry_list:
        word = word + globals()[entry + str(counter)]['text']
        if globals()[entry + str(counter)]['text'] in solution and word.count(word[-1]) <= solution.count(word[-1]):
            globals()[entry + str(counter)].config(bg='orange')
    submit.config(state=DISABLED)
    if globals()['first_entry' + str(counter)]['text'] + globals()['second_entry' + str(counter)]['text'] + globals()['third_entry' + str(counter)]['text'] + globals()['fourth_entry' + str(counter)]['text'] + globals()['fifth_entry' + str(counter)]['text'] == solution:
        win_popup()
    counter += 1
    if counter == 7:
        lose_popup()
    word = ''

def win_popup():
    top = Toplevel(win)
    top.geometry('100x30')
    top.title('WINNER')
    Label(top, text='YOU WIN!!', font=500).pack()
    for widget in root.winfo_children():
        if widget.winfo_class() == 'Button':
            widget.config(state=DISABLED)


def lose_popup():
    top = Toplevel(win)
    top.geometry('100x30')
    top.title('Loser')
    Label(top, text='YOU LOSE', font=500).pack()
    for widget in root.winfo_children():
        if widget.winfo_class() == 'Button':
            widget.config(state=DISABLED)

#frame = Frame(root)

first_entry1 = Label(text = '', width=5, height=5, fg='white', bg='black')
first_entry1.grid(row=0, column=1, padx=10, pady=10)
second_entry1 = Label(text='', width=5, height=5, fg='white', bg='black')
second_entry1.grid(row=0, column=2, padx=10, pady=10)
third_entry1 = Label(text='', width=5, height=5, fg='white', bg='black')
third_entry1.grid(row=0, column=3, padx=10, pady=10)
fourth_entry1 = Label(text='', width=5, height=5, fg='white', bg='black')
fourth_entry1.grid(row=0, column=4, padx=10, pady=10)
fifth_entry1 = Label(text='', width=5, height=5, fg='white', bg='black')
fifth_entry1.grid(row=0, column=5, padx=10, pady=10)

first_entry2 = Label(text = '', width=5, height=5, fg='white', bg='black')
first_entry2.grid(row=10, column=1, padx=10, pady=10)
second_entry2 = Label(text='', width=5, height=5, fg='white', bg='black')
second_entry2.grid(row=10, column=2, padx=10, pady=10)
third_entry2 = Label(text='', width=5, height=5, fg='white', bg='black')
third_entry2.grid(row=10, column=3, padx=10, pady=10)
fourth_entry2 = Label(text='', width=5, height=5, fg='white', bg='black')
fourth_entry2.grid(row=10, column=4, padx=10, pady=10)
fifth_entry2 = Label(text='', width=5, height=5, fg='white', bg='black')
fifth_entry2.grid(row=10, column=5, padx=10, pady=10)

first_entry3 = Label(text = '', width=5, height=5, fg='white', bg='black')
first_entry3.grid(row=20, column=1, padx=10, pady=10)
second_entry3 = Label(text='', width=5, height=5, fg='white', bg='black')
second_entry3.grid(row=20, column=2, padx=10, pady=10)
third_entry3 = Label(text='', width=5, height=5, fg='white', bg='black')
third_entry3.grid(row=20, column=3, padx=10, pady=10)
fourth_entry3 = Label(text='', width=5, height=5, fg='white', bg='black')
fourth_entry3.grid(row=20, column=4, padx=10, pady=10)
fifth_entry3 = Label(text='', width=5, height=5, fg='white', bg='black')
fifth_entry3.grid(row=20, column=5, padx=10, pady=10)

first_entry4 = Label(text = '', width=5, height=5, fg='white', bg='black')
first_entry4.grid(row=30, column=1, padx=10, pady=10)
second_entry4 = Label(text='', width=5, height=5, fg='white', bg='black')
second_entry4.grid(row=30, column=2, padx=10, pady=10)
third_entry4 = Label(text='', width=5, height=5, fg='white', bg='black')
third_entry4.grid(row=30, column=3, padx=10, pady=10)
fourth_entry4 = Label(text='', width=5, height=5, fg='white', bg='black')
fourth_entry4.grid(row=30, column=4, padx=10, pady=10)
fifth_entry4 = Label(text='', width=5, height=5, fg='white', bg='black')
fifth_entry4.grid(row=30, column=5, padx=10, pady=10)

first_entry5 = Label(text = '', width=5, height=5, fg='white', bg='black')
first_entry5.grid(row=40, column=1, padx=10, pady=10)
second_entry5 = Label(text='', width=5, height=5, fg='white', bg='black')
second_entry5.grid(row=40, column=2, padx=10, pady=10)
third_entry5 = Label(text='', width=5, height=5, fg='white', bg='black')
third_entry5.grid(row=40, column=3, padx=10, pady=10)
fourth_entry5 = Label(text='', width=5, height=5, fg='white', bg='black')
fourth_entry5.grid(row=40, column=4, padx=10, pady=10)
fifth_entry5 = Label(text='', width=5, height=5, fg='white', bg='black')
fifth_entry5.grid(row=40, column=5, padx=10, pady=10)

first_entry6 = Label(text = '', width=5, height=5, fg='white', bg='black')
first_entry6.grid(row=50, column=1, padx=10, pady=10)
second_entry6 = Label(text='', width=5, height=5, fg='white', bg='black')
second_entry6.grid(row=50, column=2, padx=10, pady=10)
third_entry6 = Label(text='', width=5, height=5, fg='white', bg='black')
third_entry6.grid(row=50, column=3, padx=10, pady=10)
fourth_entry6 = Label(text='', width=5, height=5, fg='white', bg='black')
fourth_entry6.grid(row=50, column=4, padx=10, pady=10)
fifth_entry6 = Label(text='', width=5, height=5, fg='white', bg='black')
fifth_entry6.grid(row=50, column=5, padx=10, pady=10)


letterA = Button(root, text='A', width=1, height=1, command=lambda: button_press('A'))
letterA.grid(row=60, column=0)
letterB = Button(root, text='B', width=1, height=1, command=lambda: button_press('B'))
letterB.grid(row=60, column=1)
letterC = Button(root, text='C', width=1, height=1, command=lambda: button_press('C'))
letterC.grid(row=60, column=2)
letterD = Button(root, text='D', width=1, height=1, command=lambda: button_press('D'))
letterD.grid(row=60, column=3)
letterE = Button(root, text='E', width=1, height=1, command=lambda: button_press('E'))
letterE.grid(row=60, column=4)
letterF = Button(root, text='F', width=1, height=1, command=lambda: button_press('F'))
letterF.grid(row=60, column=5)
letterG = Button(root, text='G', width=1, height=1, command=lambda: button_press('G'))
letterG.grid(row=60, column=6)

letterH = Button(root, text='H', width=1, height=1, command=lambda: button_press('H'))
letterH.grid(row=65, column=0)
letterI = Button(root, text='I', width=1, height=1, command=lambda: button_press('I'))
letterI.grid(row=65, column=1)
letterJ = Button(root, text='J', width=1, height=1, command=lambda: button_press('J'))
letterJ.grid(row=65, column=2)
letterK = Button(root, text='K', width=1, height=1, command=lambda: button_press('K'))
letterK.grid(row=65, column=3)
letterL = Button(root, text='L', width=1, height=1, command=lambda: button_press('L'))
letterL.grid(row=65, column=4)
letterM = Button(root, text='M', width=1, height=1, command=lambda: button_press('M'))
letterM.grid(row=65, column=5)
letterN = Button(root, text='N', width=1, height=1, command=lambda: button_press('N'))
letterN.grid(row=65, column=6)

letterO = Button(root, text='O', width=1, height=1, command=lambda: button_press('O'))
letterO.grid(row=70, column=0)
letterP = Button(root, text='P', width=1, height=1, command=lambda: button_press('P'))
letterP.grid(row=70, column=1)
letterQ = Button(root, text='Q', width=1, height=1, command=lambda: button_press('Q'))
letterQ.grid(row=70, column=2)
letterR = Button(root, text='R', width=1, height=1, command=lambda: button_press('R'))
letterR.grid(row=70, column=3)
letterS = Button(root, text='S', width=1, height=1, command=lambda: button_press('S'))
letterS.grid(row=70, column=4)
letterT = Button(root, text='T', width=1, height=1, command=lambda: button_press('T'))
letterT.grid(row=70, column=5)
letterU = Button(root, text='U', width=1, height=1, command=lambda: button_press('U'))
letterU.grid(row=70, column=6)

letterV = Button(root, text='V', width=1, height=1, command=lambda: button_press('V'))
letterV.grid(row=75, column=0)
letterW = Button(root, text='W', width=1, height=1, command=lambda: button_press('W'))
letterW.grid(row=75, column=1)
letterX = Button(root, text='X', width=1, height=1, command=lambda: button_press('X'))
letterX.grid(row=75, column=2)
letterY = Button(root, text='Y', width=1, height=1, command=lambda: button_press('Y'))
letterY.grid(row=75, column=3)
letterZ = Button(root, text='Z', width=1, height=1, command=lambda: button_press('Z'))
letterZ.grid(row=75, column=4)
delete = Button(root, text='Del', width=2, height=1, command=delete_button)
delete.grid(row=75, column=5)
submit = Button(root, text='Enter', width=3, height=1, command=submit_button, state=DISABLED)
submit.grid(row=75, column=6)

win = Label(text='YOU WIN!!')


root.mainloop()