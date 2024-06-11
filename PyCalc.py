#-------------------------------------------------------------------------------
# Name:        PyCalc
# Purpose:     My Second Task as a Python Programming Intern at CodSoft.
#
# Author:      Harpal
#
#-------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import math

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = str(eval(expression))
            input_text.set(" " + expression + " ")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_text.set(" " + expression + " ")
    elif text == "AC":
        expression = ""
        input_text.set(" " + expression + " ")
    elif text == "√":
        try:
            expression = str(math.sqrt(float(expression)))
            input_text.set(" " + expression + " ")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_text.set(" " + expression + " ")
    elif text == "x²":
        try:
            expression = str(float(expression) ** 2)
            input_text.set(" " + expression + " ")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_text.set(" " + expression + " ")
    elif text == "%":
        try:
            expression = str(float(expression) / 100)
            input_text.set(" " + expression + " ")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_text.set(" " + expression + " ")
    elif text == "<":
        expression = expression[:-1]
        input_text.set(" " + expression + " ")
    else:
        expression += text
        input_text.set(" " + expression + " ")

expression = ""

root = tk.Tk()
root.title("Calculator")
root.geometry("350x580")
root.configure(bg="#131315")

input_text = tk.StringVar()
input_frame = tk.Frame(root, bd=0, bg="#131315")
input_frame.pack(side=tk.TOP, padx=10, pady=10)

input_field = tk.Entry(input_frame, font=("Helvetica", 20, "bold"), textvariable=input_text, bd=1, relief=tk.FLAT, width=20, bg="#2b2b2f", fg="#dce2f9", justify="right")
input_field.grid(row=0, column=0, columnspan=4, ipady=16)

button_frame = tk.Frame(root, bg="#131315")
button_frame.pack(padx=10, pady=10)

buttons = [
    ["AC", "√", "x²", "%"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "+"],
    [".", "0", "<", "-"],
    ["="]
]

btn_colors = {
    "AC": "#4e505f",
    "√": "#7865f8",
    "x²": "#7865f8",
    "%": "#7865f8",
    "/": "#7865f8",
    "*": "#7865f8",
    "-": "#7865f8",
    "+": "#7865f8",
    "=": "#7865f8",
    ".": "#1b1c1e",
    "0": "#1b1c1e",
    "1": "#1b1c1e",
    "2": "#1b1c1e",
    "3": "#1b1c1e",
    "4": "#1b1c1e",
    "5": "#1b1c1e",
    "6": "#1b1c1e",
    "7": "#1b1c1e",
    "8": "#1b1c1e",
    "9": "#1b1c1e",
    "C": "#1b1c1e"
}


row = 1
col = 0

for button_row in buttons:
    col = 0
    for button in button_row:
        if button == "=":
            btn = tk.Button(button_frame, text=button, font=("Helvetica", 18, "bold"), bd=0, relief=tk.FLAT, width=20, height=1,
                            bg=btn_colors[button], fg="#dce2f9", activebackground=btn_colors[button], activeforeground="#dce2f9",
                            highlightbackground="#131315", highlightcolor="#131315", borderwidth=1)
            btn.grid(row=row, column=col, columnspan=4, padx=5, pady=5, ipadx=1, ipady=10)
        else:
            btn = tk.Button(button_frame, text=button, font=("Helvetica", 18, "bold"), bd=0, relief=tk.FLAT, width=4, height=1,
                            bg=btn_colors[button], fg="#dce2f9", activebackground=btn_colors[button], activeforeground="#7865f8",
                            highlightbackground="#131315", highlightcolor="#131315", borderwidth=1)
            btn.grid(row=row, column=col, padx=5, pady=5, ipadx=1, ipady=10)
            col += 1
        btn.bind("<Button-1>", click)
    row += 1

root.mainloop()
