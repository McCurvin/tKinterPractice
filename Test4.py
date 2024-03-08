import tkinter as love
from tkinter import ttk as XD

GUI = love.Tk()
GUI.title("Program Selection")
GUI.geometry("300x200")

def show_program(event):
    selectedProgram.set(f"Selected Program/Course: {program_combobox.get()}")

selectedProgram = love.StringVar()

#Create Combobox
program_combobox = XD.Combobox(GUI, values=["BSCS", "BSIT", "BSCE", "BSEE", "BSME", "BSIS"])
program_combobox.pack(padx=10,pady=10)
program_combobox.bind("<<ComboboxSelected>>",show_program)

selectedLabel = XD.Label(GUI,textvariable=selectedProgram)
selectedLabel.pack()

GUI.mainloop()