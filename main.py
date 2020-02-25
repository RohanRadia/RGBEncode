# Interface
# 15 + 575 + 70 + 575 + 15 for top boxes
import tkinter
from tkinter.filedialog import askopenfilename


class GUI:
    def __init__(self):
        self.file_name = None

    def open_file_menu(self):
        filename = askopenfilename()
        self.file_name = filename

    def run(self):
        root = tkinter.Tk()

        """Basic Background"""
        canvas = tkinter.Canvas(root, bg="grey", width=1250, height=660)
        canvas.pack()

        """Text Input Box"""
        text_input = tkinter.Text(canvas, width=70, height=22)
        text_input.place(x=15, y=15)
        text_input.insert(tkinter.INSERT, "Enter text here...")

        """Output Box"""
        text_output = tkinter.Text(canvas, width=70, height=22)
        text_output.place(x=674, y=15)

        """Arrow"""
        set_y = 185
        canvas.create_line(600, set_y, 650, set_y, arrow=tkinter.LAST)

        """Choose File"""
        choose_file = tkinter.Button(canvas, text="Choose File", command=self.open_file_menu)
        choose_file.place(x=15, y=385)

        """Run Button"""
        run = tkinter.Button(canvas, text="Run")
        run.place(x=610, y=480)

        """Encryption Key Input Box"""
        text_input = tkinter.Text(canvas, width=70, height=2)
        text_input.place(x=15, y=423)
        text_input.insert(tkinter.INSERT, "Enter encryption key here...")

        """URL Input Box"""
        text_input = tkinter.Text(canvas, width=70, height=2)
        text_input.place(x=15, y=563)
        text_input.insert(tkinter.INSERT, "Enter base URL here...")

        """URL Output Box"""
        text_input = tkinter.Text(canvas, width=70, height=2)
        text_input.place(x=675, y=563)

        """Arrow Two"""
        set_y = 581
        canvas.create_line(600, set_y, 650, set_y, arrow=tkinter.LAST)

        """Shorten Button"""
        run = tkinter.Button(canvas, text="Shorten")
        run.place(x=600, y=620)

        root.mainloop()


new_GUI = GUI()
new_GUI.run()
