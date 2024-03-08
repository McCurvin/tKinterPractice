from tkinter import Tk, Text

gui = Tk()
gui.resizable(False, False)
gui.title("Text	Widget	Example")

text = Text(gui, height=8, state="disabled")
text.pack()


gui.mainloop()