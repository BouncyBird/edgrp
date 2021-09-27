import random
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox
from pathlib import Path
import os
import sys
from listof import people
from playsound import playsound
import time


def genf():
    u = 0

    def home():
        os.execl(sys.executable, sys.executable, *sys.argv)

    choice = random.choice(people)
    if Path("picked.txt").exists() == False:
        newfile = open("picked.txt", "w")
        newfile.close()
    pfile = open("picked.txt")
    pcon = pfile.read()
    while choice in pcon:
        choice = random.choice(people)
    pfile = open("picked.txt", "a")
    pfile.write(choice + "\n")
    pfile.close()
    hb = tk.Button(root, text="Home", width=10,
                   height=1, fg="black", command=home)
    hb.pack()
    gen.pack_forget()
    rb.pack_forget()
    playsound('music.mp3')
    pickedtext = Text(root)
    pickedtext.insert(INSERT, choice)
    pickedtext.pack()


def rbf():
    result = tkinter.messagebox.askquestion(
        "Reset", "Are You Sure?", icon="warning")
    if result == "yes":
        pfile = open("picked.txt", "w")
        pfile.close()
    else:
        print("Not Resetted")


root = tk.Tk()
root.geometry("700x600")
root.title("EDG Random Picker")

wl = tk.Label(
    text="Welcome!\nTo EDG Random Picker", fg="black", font=("Calibri", 36, "bold")
)
wl.pack(padx=0, pady=55)

gen = tk.Button(root, text="Generate", width=20,
                height=3, fg="black", command=genf)
gen.pack()

rb = tk.Button(root, text="Reset", width=20, height=3, fg="black", command=rbf)
rb.pack()


root.mainloop()
