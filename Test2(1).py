import tkinter as love
from tkinter import ttk as XD

GUI = love.Tk()
GUI.geometry("300x200")
GUI.title("Gender Selection")

def show_gender():
    selectedGender.set(f"Selected Gender: {gender.get()}")

#Storevalue
selectedGender = love.StringVar()

selectedLabel = XD.Label(GUI, textvariable=selectedGender)
selectedLabel.pack(pady=10)

#GenderFrame
genderFrame = XD.LabelFrame(GUI, text="Select Gender:")
genderFrame.pack()

#Genders
gender = love.StringVar()

#male
maleRadio = XD.Radiobutton(genderFrame, text="Male",variable=gender,value="Male")
maleRadio.grid(row=0,column=0,padx=10,pady=5,sticky="w")

#female
femaleRadio = XD.Radiobutton(genderFrame, text="Female",variable=gender,value="Female", command=show_gender)
femaleRadio.grid(row=1,column=0,padx=10,pady=5,sticky="w")

#Initial
gender.set("Male")
show_gender()

GUI.mainloop()



