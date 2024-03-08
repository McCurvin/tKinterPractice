import tkinter as love
from tkinter import ttk as XD

GUI = love.Tk()
GUI.title("Spinbox Example")
GUI.geometry("300x200")

def updateValue():
    selectedValue.set(spinBox.get())

selectedValue = love.StringVar()

spinBox = XD.Spinbox(GUI, from_=0,to=100,textvariable=selectedValue,command=updateValue)
spinBox.pack(padx=10,pady=10)

valueLabel = XD.Label(GUI, textvariable=selectedValue)
valueLabel.pack()

GUI.mainloop()