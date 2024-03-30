from tkinter import *
from keypress_sound import keypress_sound

typewriter_sfx = True  # set to False to disable typewriter sound effects

sleep_timer = 1
timer = 0

window = Tk()

text = ""

# constants
INACTIVE_COlOR = "#9bd7d1"
ACTIVE_COLOR = "#f9a36c"
BG_COLOR = "#305d7a"
FONT_NAME = "Quicksand"


def key_event(event) -> None:
    global text
    global timer
    if event.keysym == "BackSpace":
        text = text[0:-1]
    else:
        text += event.char
    lbl.config(text=text, fg=ACTIVE_COLOR)
    timer = 0
    update_font_size()
    if not typewriter_sfx:
        return
    keypress_sound()


def update_font_size():
    lines = lbl["text"].split("\r")
    num_lines = len(lines)
    longest_len = len(max(lines, key=len))
    ev_width, ev_height = window.winfo_width(), window.winfo_height()
    font_size_width = max(ev_width // (longest_len + 1), 1)
    font_size_height = max(ev_height // num_lines, 1)
    font_size = min(font_size_width, font_size_height)
    lbl.config(font=(FONT_NAME, font_size))


def increment_timer() -> None:
    global text
    global timer
    if window.option_get("lbl", "text") != "<key>":
        if timer < sleep_timer:
            timer += 0.5
        elif timer >= sleep_timer:
            lbl.config(text="<key>", fg=INACTIVE_COlOR)
            update_font_size()
            text = ""
        window.after(500, increment_timer)


increment_timer()

window.bind("<Key>", key_event)

lbl = Label(
    master=window,
    text="<key>",
    font=(FONT_NAME, window.winfo_height()),
    fg=INACTIVE_COlOR,
    bg=BG_COLOR,
)
lbl.pack(
    expand=True,
    fill="both",
)


def on_resize(event):
    update_font_size()


window.state("zoomed")
window.bind("<Configure>", on_resize)

window.attributes("-fullscreen", True)


def toggle_fullscreen(event) -> None:
    match window.attributes("-fullscreen"):

        case 1:
            window.attributes("-fullscreen", False)
        case 0:
            if event.keycode == 70:
                window.attributes("-fullscreen", True)
                return
            window.destroy()


window.bind("<Escape>", toggle_fullscreen)

window.bind("<Control-f>", toggle_fullscreen)

window.mainloop()
