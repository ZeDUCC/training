import itertools
import tkinter
import random
from tkinter import *

moves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "switch", "back/forth", "pull"]

#1: left head turning kick
#2: right head turning kick
#3: left body turning kick
#4: right body turning kick
#5: left head side kick
#6: right head side kick
#7: left head hook kick
#8: right head hook kick
#9: back kick
#10: 360 turning kick

combos = list(itertools.permutations(moves, 5))

top = tkinter.Tk()

top.geometry("1920x1080")
top.title("taekwondo combos")

txt_output = Text(top, height=50, width=300, font=('Helvetica', 55, 'bold'))
txt_output.tag_add("center", "1.0", "end")
txt_output.pack(pady=0)

for i in range(20):
    txt_output.insert(END, str(random.choice(combos)) + "\n")

top.mainloop()