import tkinter as tk


window = tk.Tk()
window.title("moving window 1 :)")
window.geometry("300x300+300+300")  # Initial position
window.update()

window2 = tk.Tk()
window2.title("moving window 2 :)")
window2.geometry("300x300+300+700")  # Initial position
window2.update()


def zig(window, name) -> None:
    if name.get():
        name.set(False)
    else:
        name.set(True)
    window.after(1000, lambda: zig(window, name))


windows = {}
windows.update(dict(x for x in locals().items() if type(x[1]) in (tk.Tk, tk.Toplevel)))


def move_window(window, name):
    speed = 10
    widthxheight = f"300x300"
    if name.get() is True:
        loc = f"{widthxheight}+{window.winfo_x()+speed}+{window.winfo_y()-speed}"
    else:
        loc = f"{widthxheight}+{window.winfo_x()+speed}+{window.winfo_y()+speed}"
    window.geometry(loc)
    window.after(
        100, lambda: move_window(window, name)
    )  # Auto call to move_window again every 1/2 second


for window in windows.values():
    name = window.title()
    name = tk.BooleanVar(master=window, value=False)
    zig(window, name)
    move_window(window, name)

window.mainloop()
