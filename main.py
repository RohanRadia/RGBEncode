# Interface
# 15 + 575 + 70 + 575 + 15 for top boxes
import tkinter

from tkinter.filedialog import askopenfilename

from RGBEncode import RGBEncode
from Utils.Misc import shorten_url


class GUI:
    def __init__(self):
        self.canvas = None
        self.file_name = None
        self.file_type = None

    def choice(self,
               raw_data,
               encryption_key,
               output_frame_name):

        if self.file_name is not None and self.file_name.startswith("File chosen: "):
            self.file_name = self.file_name[13:]

        chooser = RGBEncode(raw_data, self.file_name, self.file_type, encryption_key, output_frame_name)
        chooser.call_run()

    def deselect_file_menu(self, text_input, choose_button, deselect_button):
        self.file_name = None
        self.file_type = None

        text_input.configure(state="normal")
        text_input.delete('1.0', tkinter.END)
        text_input.insert(tkinter.INSERT, "[Enter text here]")

        choose_button.configure(state="normal")
        deselect_button.place_forget()

    def open_file_menu(self, text_input, choose_button):
        filename = askopenfilename()
        self.file_name = filename

        if self.file_name is not '':
            text_input.delete('1.0', tkinter.END)
            text_input.insert(tkinter.INSERT, f"File chosen: {self.file_name}")
            text_input.configure(state="disabled")

            self.file_type = self.file_name.split(".")[-1]

            choose_button.configure(state="disabled")

            deselect_file = tkinter.Button(self.canvas, text="De-Select File",)
            deselect_file.configure(command=lambda: self.deselect_file_menu(text_input,
                                                                            choose_button,
                                                                            deselect_file))
            deselect_file.place(x=115, y=385)

    @staticmethod
    def shortening_button(url, output_box):
        shortened = shorten_url(url)

        output_box.configure(state="normal")
        output_box.delete("1.0", tkinter.END)
        output_box.insert(tkinter.INSERT, shortened)
        output_box.configure(state="disabled")

    def gui(self):
        root = tkinter.Tk()

        """Basic Background"""
        canvas = tkinter.Canvas(root, bg="grey", width=1250, height=660)
        canvas.pack()
        self.canvas = canvas

        """Text Input Box"""
        text_input = tkinter.Text(canvas, width=70, height=22)
        text_input.place(x=15, y=15)
        text_input.insert(tkinter.INSERT, "[Enter text here]")

        """Output Box"""
        text_output = tkinter.Text(canvas, width=70, height=22)
        text_output.place(x=674, y=15)
        text_output.configure(state="disabled")

        """Arrow"""
        set_y = 185
        canvas.create_line(600, set_y, 650, set_y, arrow=tkinter.LAST)

        """Choose File"""
        choose_file = tkinter.Button(canvas, text="Choose File")
        choose_file.configure(command=lambda: self.open_file_menu(text_input, choose_file))
        choose_file.place(x=15, y=385)

        """Encryption Key Input Box"""
        encryption_input = tkinter.Text(canvas, width=70, height=2)
        encryption_input.place(x=15, y=423)
        encryption_input.insert(tkinter.INSERT, "[Enter encryption key here]")

        """File Name Input Box"""
        file_name_input = tkinter.Text(canvas, width=70, height=2)
        file_name_input.place(x=674, y=423)
        file_name_input.insert(tkinter.INSERT, "[Enter what you would like the encoded frame to be named]")

        """URL Input Box"""
        url_input = tkinter.Text(canvas, width=70, height=2)
        url_input.place(x=15, y=563)
        url_input.insert(tkinter.INSERT, "Enter base URL here...")

        """URL Output Box"""
        url_output = tkinter.Text(canvas, width=70, height=2)
        url_output.place(x=675, y=563)
        url_output.configure(state="disabled")

        """Arrow Two"""
        set_y = 581
        canvas.create_line(600, set_y, 650, set_y, arrow=tkinter.LAST)

        """Shorten Button"""
        shorten_run = tkinter.Button(canvas, text="Shorten")
        shorten_run.configure(command=lambda: self.shortening_button(url_input.get("1.0", tkinter.END),
                                                                     url_output))
        shorten_run.place(x=600, y=620)

        """Run Button"""
        run = tkinter.Button(canvas, text="Run")
        run.configure(command=lambda: self.choice(text_input.get("1.0", tkinter.END),
                                                  encryption_input.get("1.0", tkinter.END),
                                                  file_name_input.get("1.0", tkinter.END)))
        run.place(x=610, y=480)

        root.mainloop()

    def run(self):
        self.gui()


new_GUI = GUI()
new_GUI.run()
