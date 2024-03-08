import tkinter as tk
from tkinter import ttk


def on_select():
    selected_items = listbox.curselection()  # Get	the	indices	of	selected	items
    selected_text = [listbox.get(i) for i in selected_items]  # Get	the	selected	item(s)
    selection_label.config(text=f"Selected	Item(s): {', '.join(selected_text)}")


# Create the main GUI window
gui = tk.Tk()
gui.title("Listbox Example")

# Create a Listbox
listbox = tk.Listbox(gui, selectmode=tk.SINGLE)  # Allows	multiple	item	selection
listbox.pack(padx=10, pady=10)

# Add items	to the Listbox
items = ["Cupcake", "Donut", "Eclair", "Froyo", "Gingerbread"]
for item in items:
    listbox.insert(tk.END, item)  # Insert	items	at	the	end	of	the	Listbox

#Create	a Button to	get	the	selected item(s)
get_selected_button = ttk.Button(gui, text="Get Selected", command=on_select)
get_selected_button.pack(pady=5)


#Create	a Label	to	display	the	selected item(s)
selection_label = ttk.Label(gui, text="Selected	Item(s):")
selection_label.pack()


gui.mainloop()
