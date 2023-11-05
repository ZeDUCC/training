import itertools
import tkinter
import random
from tkinter import *

moves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "bob", "slip", "pull"]

#1: jab
#2: cross
#3: lead hook
#4: rear hook
#5: lead uppercut
#6: rear uppercut
#7: left body hook
#8: right body hook
#9: body jab
#10: body hook

combos = list(itertools.permutations(moves, 5))

top = tkinter.Tk()

top.geometry("1920x1080")
top.title("boxing combos")

txt_output = Text(top, height=50, width=300, font=('Helvetica', 55, 'bold'))
txt_output.tag_add("center", "1.0", "end")
txt_output.pack(pady=0)

for i in range(20):
    txt_output.insert(END, str(random.choice(combos)) + "\n")

top.mainloop()