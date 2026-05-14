from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry box
entry = Entry(root, width=20, font=("Arial", 20), borderwidth=5, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to click buttons
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Clear screen
def button_clear():
    entry.delete(0, END)

# Calculate result
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button design
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:

    action = lambda x=button: (
        button_clear() if x == 'C'
        else button_equal() if x == '='
        else button_click(x)
    )

    Button(root,
           text=button,
           width=5,
           height=2,
           font=("Arial", 18),
           command=action).grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col > 3:
        col = 0
        row += 1

# Run app
root.mainloop()
