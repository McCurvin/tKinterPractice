import tkinter as love
from tkinter import ttk as XD
from tkinter.messagebox import showinfo

GUI = love.Tk()
GUI.geometry("300x200")
GUI.title("Checkbox Demo")

result = love.StringVar()

def hobbies_changed():
    showinfo(title="Hobbies", message=result.get())

XD.Checkbutton(
    GUI,
    text="Eat",
    command=hobbies_changed,
    variable=result,
    onvalue="Eat",
    offvalue="Do not Eat"
).pack()

XD.Checkbutton(
    GUI,
    text="Sleep",
    command=hobbies_changed,
    variable=result,
    onvalue="Sleep",
    offvalue="Do not Sleep"
).pack()

XD.Checkbutton(
    GUI,
    text="Pray",
    command=hobbies_changed,
    variable=result,
    onvalue="Pray",
    offvalue="Do not Pray"
).pack()

GUI.mainloop()