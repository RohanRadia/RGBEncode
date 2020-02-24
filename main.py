# Interface
# 15 + 575 + 70 + 575 + 15 for top boxes
import tkinter
from PIL import ImageTk, Image

root = tkinter.Tk()

"""Basic Background"""
canvas = tkinter.Canvas(root, bg="grey", width=1250, height=750)
canvas.pack()

"""Text Inpupt Box"""
text_input = tkinter.Text(canvas, width=70, height=22)
text_input.place(x=15, y=15)
text_input.insert(tkinter.INSERT, "Enter text here...")

"""Output Box"""
text_output = tkinter.Text(canvas, width=70, height=22)
text_output.place(x=674, y=15)
text_output.insert(tkinter.INSERT, "")

"""Arrow"""
set_y = 185
canvas.create_line(600, set_y, 650, set_y, arrow=tkinter.LAST)

"""Choose File"""

"""Run Button"""
run = tkinter.Button(canvas, text="Run")
run.place(x=610, y=200)

"""Encryption Key Input Box"""
text_input = tkinter.Text(canvas, width=70, height=2)
text_input.place(x=15, y=385)
text_input.insert(tkinter.INSERT, "Enter encryption key here...")

"""URL Input Box"""

"""URL Output Box"""

"""Shorten Button"""

root.mainloop()
