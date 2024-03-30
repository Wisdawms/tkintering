from tkinter import *

ZERO_DIV_ERROR_MSG = "Can't divide by zero!"
SYNTAX_ERROR_MSG = "Syntax error!"

FONT_NAME = "Fixedsys"


def button_press(num):
    global equation_text
    if equation_label.get() in (ZERO_DIV_ERROR_MSG, SYNTAX_ERROR_MSG):
        equation_text = ""
        equation_label.set(equation_text)
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals() -> None:
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set(ZERO_DIV_ERROR_MSG)
    except SyntaxError:
        equation_label.set(SYNTAX_ERROR_MSG)


def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)


window = Tk()

window.title("Calculator Program")

window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(
    master=window,
    textvariable=equation_label,
    font=(FONT_NAME, 24),
    bg="white",
    width=24,
    height=2,
)
label.pack()

frame = Frame(master=window)
frame.pack(expand=True)

# buttons
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for index, symbol in enumerate(numbers):
    row = index // 3
    column = index % 3
    button = Button(
        frame,
        text=symbol,
        height=4,
        width=9,
        font=35,
        command=lambda bt=symbol: button_press(bt),
    )
    button.grid(row=row, column=column)

plus = Button(
    frame,
    text="+",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("+"),
)
plus.grid(row=0, column=4)

minus = Button(
    frame,
    text="-",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("-"),
)
minus.grid(row=1, column=4)

minus = Button(
    frame,
    text="*",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("*"),
)
minus.grid(row=2, column=4)

divide = Button(
    frame,
    text="/",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("/"),
)
divide.grid(row=3, column=4)

equal = Button(
    frame,
    text="=",
    height=4,
    width=9,
    font=35,
    command=equals,
)
equal.grid(row=3, column=2)

decimal = Button(
    frame,
    text=".",
    height=4,
    width=9,
    font=35,
    command=lambda: button_press("."),
)
decimal.grid(row=3, column=1)

clear = Button(
    frame,
    text="CLEAR",
    height=4,
    width=(9 * 2) + 9,
    font=35,
    command=clear,
)
clear.grid(row=4, column=0, columnspan=6)

for child in frame.winfo_children():
    child.config(font=("Fixedsys", 24))

window.mainloop()
