from io import TextIOWrapper
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
from keypress_sound import keypress_sound

typewriter_sfx = True  # set to False to disable typewriter sound effects


def key_event(event) -> None:
    if not typewriter_sfx:
        return
    keypress_sound()


current_file = "untitled.txt"

DEFAULT_FONT_NAME = "Small Fonts"
DEFAULT_FONT_SIZE = 32
old_size = DEFAULT_FONT_SIZE


def change_bg_color(event) -> None:
    bg_color = colorchooser.askcolor(title="Pick a background color")
    text_area.config(bg=bg_color[1])


def change_fg_color(event) -> None:
    fg_color = colorchooser.askcolor(title="Pick a foreground color")
    text_area.config(fg=fg_color[1])


def change_font(*args):
    global old_size
    try:
        if font_size.get():
            text_area.config(font=(font_name.get(), font_size.get()))
            file_menu.config(font=(font_name.get(), font_size.get()))
            edit_menu.config(font=(font_name.get(), font_size.get()))
            help_menu.config(font=(font_name.get(), font_size.get()))
            old_size = font_size.get()
        else:
            font_size.set(old_size)
            change_font()
    except Exception as e:
        print(e)
        font_size.set(old_size)
        change_font()


def new_file(event) -> None:
    global current_file
    current_file = ""
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file(event) -> None:
    global current_file
    file = askopenfilename(
        defaultextension=".txt", file=[("All Files", "*.*"), ("Text Files", "*.txt")]
    )
    try:
        if file != "":
            current_file = file
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)
            file = open(file, "r")
            text_area.insert(1.0, file.read())
    except:
        return
    finally:
        if file is TextIOWrapper:
            file.close()


def save_file(event) -> None:
    global current_file
    if (
        type(event) is Event
        and os.path.exists(current_file)
        and type(event)
        and event.state == 12
    ) or (type(event) is not Event and os.path.exists(current_file) and event == "ow"):
        print("OVERWRITE")
        file = open(current_file, "w+")
        file.write(text_area.get(1.0, END))
        file.close()
        return
    file = filedialog.asksaveasfilename(
        initialfile="untitled.txt",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    current_file = file
    if file != "":
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
        except:
            return
        finally:
            if file is TextIOWrapper:
                file.close()
    else:
        current_file = "untitled.txt"


def cut(event) -> None:
    text_area.event_generate("<<Cut>>")


def copy(event) -> None:
    text_area.event_generate("<<Copy>>")


def paste(event) -> None:
    text_area.event_generate("<<Paste>>")


def about() -> None:
    showinfo("About this program", "This is a program written by you!")


def quit() -> None:
    window.destroy()


window = Tk()
window.title("Text Editor Program")
file = None
window_width, window_height = 500, 500
screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(master=window)
font_name.set(DEFAULT_FONT_NAME)

font_size = StringVar(master=window)
font_size.set(DEFAULT_FONT_SIZE)

text_area = Text(master=window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(master=text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(
    yscrollcommand=scroll_bar.set,
    bg="#141f1d",
    fg="#b59e6c",
    insertbackground="white",
    insertwidth=4,
    insertofftime=250,
)

frame = Frame(master=window)
frame.grid()

bg_color_button = Button(
    master=frame,
    text="bg_color",
    command=lambda: change_bg_color(None),
    height=5,
    width=20,
)
bg_color_button.grid(row=0, column=0)

fg_color_button = Button(
    master=frame,
    text="fg_color",
    command=lambda: change_fg_color(None),
    height=5,
    width=20,
)
fg_color_button.grid(row=0, column=1)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=2)

size_box = Spinbox(
    frame, from_=1, to=100, textvariable=font_size, command=change_font, increment=5
)
size_box.grid(row=0, column=3)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font=(font_name.get(), font_size.get()))
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New (Ctrl+N)", command=lambda: new_file(None))
file_menu.add_command(label="Open (Ctrl+O)", command=lambda: open_file(None))
file_menu.add_command(label="Save (Ctrl+S)", command=lambda: save_file("ow"))
file_menu.add_command(label="Save As.. (Ctrl+Shift+S)", command=lambda: save_file(None))
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0, font=(font_name.get(), font_size.get()))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut (Ctrl+X)", command=lambda: cut(None))
edit_menu.add_command(label="Copy (Ctrl+C)", command=lambda: copy(None))
edit_menu.add_command(label="Paste (Ctrl+V)", command=lambda: paste(None))

help_menu = Menu(menu_bar, tearoff=0, font=(font_name.get(), font_size.get()))
menu_bar.add_cascade(label="Edit", menu=help_menu)

help_menu.add_command(label="About", command=about)

window.bind("<Key>", key_event)

# shortcuts
window.bind("<Control-n>", new_file)
window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file)
window.bind("<Shift-Alt-S>", save_file)

window.bind("<Control-x>", cut)
window.bind("<Control-c>", copy)
window.bind("<Control-v>", paste)

size_box.bind("<Return>", change_font)

window.state("zoomed")

text_area.focus_set()

if os.path.exists("untitled.txt"):
    try:
        window.title("untitled.txt")
        text_area.delete(1.0, END)
        file = open("untitled.txt", "r")
        text_area.insert(1.0, file.read())
    finally:
        if file is TextIOWrapper:
            file.close()

window.mainloop()
