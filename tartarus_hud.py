import tkinter as tk
import json

def save_bindings():
    bindings = {}
    for i in range(1, 21):
        bindings[f"Button {i}"] = button_vars[i].get()
    bindings["Scroll"] = scroll_var.get()
    bindings["Joystick"] = joystick_var.get()
    bindings["Thumb Button"] = thumb_var.get()
    
    with open("bindings.json", "w") as f:
        json.dump(bindings, f)

def load_bindings():
    try:
        with open("bindings.json", "r") as f:
            bindings = json.load(f)
    except FileNotFoundError:
        return
    
    for i in range(1, 21):
        button_vars[i].set(bindings.get(f"Button {i}", ""))
    scroll_var.set(bindings.get("Scroll", ""))
    joystick_var.set(bindings.get("Joystick", ""))
    thumb_var.set(bindings.get("Thumb Button", ""))

# initialize tkinter window
root = tk.Tk()
root.title("Tartarus HUD")

# initialize variables for buttons and joystick
button_vars = {}
for i in range(1, 21):
    button_vars[i] = tk.StringVar()
scroll_var = tk.StringVar()
joystick_var = tk.StringVar()
thumb_var = tk.StringVar()

# load bindings from file
load_bindings()

# create widgets for buttons 1-20
# for i in range(1, 21):
#     tk.Label(root, text=f"Button {i}:").grid(row=i-1, column=0)
#     tk.Entry(root, textvariable=button_vars[i]).grid(row=i-1, column=1)
for i in range(1, 21):
    row = (i-1) // 5
    col = (i-1) % 5
    tk.Label(root, text=f"Button {i}:").grid(row=row, column=col*2)
    tk.Entry(root, textvariable=button_vars[i]).grid(row=row, column=col*2+1)

# create widgets for scroll, joystick and thumb button
tk.Label(root, text="Scroll:").grid(row=20, column=0)
tk.Entry(root, textvariable=scroll_var).grid(row=20, column=1)

tk.Label(root, text="Joystick:").grid(row=21, column=0)
tk.Entry(root, textvariable=joystick_var).grid(row=21, column=1)

tk.Label(root, text="Thumb Button:").grid(row=22, column=0)
tk.Entry(root, textvariable=thumb_var).grid(row=22, column=1)

# create save button
tk.Button(root, text="Save", command=save_bindings).grid(row=23, column=0, columnspan=2, pady=10)

# run mainloop
root.mainloop()