import tkinter as tk
from tkinter import ttk

def page1_content():
    label1.config(text="This is Page 1")
    label2.config(text="You can add content for Page 1 here.")

def page2_content():
    label1.config(text="This is Page 2")
    label2.config(text="You can add content for Page 2 here.")

def page3_content():
    label1.config(text="This is Page 3")
    label2.config(text="You can add content for Page 3 here.")

# Create the main GUI window
gui = tk.Tk()
gui.title("Notebook Example")

# Create a Notebook widget
notebook = ttk.Notebook(gui)
notebook.pack(padx=10, pady=10)

# Create three frames as pages and add them to the Notebook
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
notebook.add(frame1, text="Page 1")
notebook.add(frame2, text="Page 2")
notebook.add(frame3, text="Page 3")

# Create labels and buttons for each page
label1 = ttk.Label(frame1, text="This is Page 1")
label1.pack(padx=10, pady=10)
button1 = ttk.Button(frame1, text="Page 1 Content", command=page1_content)
button1.pack(pady=5)

label2 = ttk.Label(frame2, text="This is Page 2")
label2.pack(padx=10, pady=10)
button2 = ttk.Button(frame2, text="Page 2 Content", command=page2_content)
button2.pack(pady=5)

label3 = ttk.Label(frame3, text="This is Page 3")
label3.pack(padx=10, pady=10)
button3 = ttk.Button(frame3, text="Page 3 Content", command=page3_content)
button3.pack(pady=5)

gui.mainloop()
