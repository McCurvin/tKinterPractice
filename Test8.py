import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress_bar.start()        # Start the progress bar animation
    for i in range(101):
        time.sleep(0.05)        # Simulate some work
        progress_var.set(i)     # Update the progress bar value
        gui.update()            # Update the GUI
    progress_bar.stop()         # Stop the progress bar animation

# Create the main GUI window
gui = tk.Tk()
gui.title("Progress Bar Example")

# Create a progress bar widget
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(gui, variable=progress_var, maximum=100)
progress_bar.pack(padx=10, pady=10)

# Create a button to start the progress
start_button = ttk.Button(gui, text="Start Progress", command=start_progress)
start_button.pack(pady=5)

gui.mainloop()
