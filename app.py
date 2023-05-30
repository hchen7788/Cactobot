import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Cactobot")

# Create label
label = tk.Label(root, text="Welcome to Cactobot")

# Create widgets
button = tk.Button(root, text="Button")
canvas = tk.Canvas(root, bg='white', width=50, height=50)
checkbutton = tk.Checkbutton(root, text="Checkbutton")
entry = tk.Entry(root, text="Entry", width=10)
frame = tk.Frame(root)
labelframe = tk.LabelFrame(root, text="LabelFrame", padx=5, pady=5)
listbox = tk.Listbox(root, height=3)
menu = tk.Menu(root)

# Lay out label
label.pack()

# Lay out widgets
button.pack(padx=5, pady=5)
canvas.pack(padx=5, pady=5)
checkbutton.pack(padx=5, pady=5)
entry.pack(padx=5, pady=5)
frame.pack(padx=5, pady=10)
# label.pack(padx=5, pady=5)
labelframe.pack(padx=5, pady=5)
listbox.pack(padx=5, pady=5)

# Run forever!
root.mainloop()

