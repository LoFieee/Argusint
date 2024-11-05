
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LoFie\Desktop\argusint\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("                                                                                                                              Argusint")

#blank image tkt bro
blank_image = PhotoImage(width=1, height=1)
window.iconphoto(False, blank_image)

window.geometry("865x753")
window.configure(bg = "#393939")


canvas = Canvas(
    window,
    bg = "#393939",
    height = 753,
    width = 865,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    432.00001525878906,
    376.0,
    image=image_image_1
)

canvas.create_text(
    145.0,
    45.0,
    anchor="nw",
    text="ARGUSINT",
    fill="#FFFFFF",
    font=("Syne ExtraBold", 64 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    799.0,
    80.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    104.0,
    80.0,
    image=image_image_3
)

canvas.create_text(
    379.0,
    121.0,
    anchor="nw",
    text="By Lofie",
    fill="#FFFFFF",
    font=("Syne ExtraBold", 16 * -1)
)

canvas.create_rectangle(
    188.0,
    162.0,
    675.0,
    672.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    188.0,
    161.0,
    675.0,
    188.0,
    fill="#BBBBBB",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    431.0,
    450.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FAFAFA",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=296.0,
    y=436.0,
    width=270.0,
    height=27.0
)

canvas.create_text(
    279.0,
    217.0,
    anchor="nw",
    text="ENTER THE FORMULA",
    fill="#000000",
    font=("Syne ExtraBold", 16 * -1)
)

canvas.create_text(
    230.0,
    628.0,
    anchor="nw",
    text="With great power, comes great responsibility...",
    fill="#000000",
    font=("Syne ExtraBold", 11 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    426.0,
    316.0,
    image=image_image_4
)

canvas.create_rectangle(
    268.0,
    435.0,
    269.0,
    465.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    582.0,
    435.0,
    583.0,
    465.0,
    fill="#000000",
    outline="")

canvas.create_text(
    277.0,
    440.0,
    anchor="nw",
    text=">",
    fill="#000000",
    font=("Syne ExtraBold", 16 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    430.0,
    573.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    474.0,
    573.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    386.0,
    573.0,
    image=image_image_7
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=386.0,
    y=489.0,
    width=91.0,
    height=19.0
)
window.resizable(False, False)
window.mainloop()
