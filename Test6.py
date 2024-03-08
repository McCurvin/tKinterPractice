import tkinter as love
from tkinter import ttk as XD

GUI = love.Tk()
GUI.title("Gender and Program Selection")

def showGender():
    selectedGender.set(f"Selected Gender: {gender.get()}")

def showProgram(event=None):
    selectedProgram.set(f"Selected Program: {program_Combobox.get()}")

# Store Gender
selectedGender = love.StringVar()  # Changed: Created selectedGender variable

# GenderFrame
genderFrame = XD.LabelFrame(GUI, text="Select Gender:")
genderFrame.pack(padx=10, pady=10)

# Store gender radio button
gender = love.StringVar()

# MaleRadio
maleRadio = XD.Radiobutton(genderFrame, text="Male", variable=gender, value="Male", command=showGender)
maleRadio.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# FemaleRadio
femaleRadio = XD.Radiobutton(genderFrame, text="Female", variable=gender, value="Female", command=showGender)
femaleRadio.grid(row=1, column=0, padx=10, pady=5, sticky="w")

gender.set("Male")
showGender()


#StoreProgram
selectedProgram = love.StringVar()

#Frame for Program
programFrame = XD.LabelFrame(GUI,text="Select Program:")
programFrame.pack(padx=10,pady=10)

program_Combobox = XD.Combobox(programFrame, values=["BSCS", "BSIT", "BSCE", "BSEE", "BSME", "BSIS"])
program_Combobox.pack(padx=10,pady=5)
program_Combobox.bind("<<ComboboxSelected>>", showProgram)

GUI.mainloop()
