
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/smarthsood/Desktop/APP4 gui/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1489.0,
    1024.0,
    fill="#063C53",
    outline="")

canvas.create_rectangle(
    57.0,
    17.0,
    1253.0,
    181.0,
    fill="#FFFCFC",
    outline="")

canvas.create_text(
    295.0,
    58.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_rectangle(
    57.0,
    232.0,
    533.0,
    335.0,
    fill="#000000",
    outline="")

canvas.create_text(
    57.0,
    235.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    0.0,
    258.0,
    anchor="nw",
    text="A",
    fill="#FFFFFF",
    font=("TruculentaRoman Regular", 40 * -1)
)

button_image_1 = PhotoImage(
    file="button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=544.0,
    y=258.0,
    width=124.0,
    height=44.0
)

button_image_hover_1 = PhotoImage(
    file="button_hover_1.png")

def button_1_hover(e):
    button_1.config(
        image=button_image_hover_1
    )
def button_1_leave(e):
    button_1.config(
        image=button_image_1
    )

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)


canvas.create_rectangle(
    179.0,
    786.0,
    1253.0,
    937.0,
    fill="#000000",
    outline="")

canvas.create_text(
    179.0,
    786.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    9.0,
    833.0,
    anchor="nw",
    text="Feedback",
    fill="#FFFFFF",
    font=("TruculentaRoman Regular", 40 * -1)
)

button_image_2 = PhotoImage(
    file="button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1264.0,
    y=830.0,
    width=124.0,
    height=44.0
)

button_image_hover_2 = PhotoImage(
    file="button_hover_2.png")

def button_2_hover(e):
    button_2.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    button_2.config(
        image=button_image_2
    )

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)


canvas.create_rectangle(
    443.0,
    632.0,
    919.0,
    735.0,
    fill="#000000",
    outline="")

canvas.create_text(
    443.0,
    635.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    269.0,
    658.0,
    anchor="nw",
    text="Answer",
    fill="#FFFFFF",
    font=("TruculentaRoman Regular", 40 * -1)
)

button_image_3 = PhotoImage(
    file="button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=930.0,
    y=658.0,
    width=124.0,
    height=44.0
)

button_image_hover_3 = PhotoImage(
    file="button_hover_4.png")

def button_3_hover(e):
    button_3.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    button_3.config(
        image=button_image_3
    )

button_3.bind('<Enter>', button_3_hover)
button_3.bind('<Leave>', button_3_leave)


canvas.create_rectangle(
    777.0,
    230.0,
    1253.0,
    333.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    57.0,
    447.0,
    533.0,
    550.0,
    fill="#000000",
    outline="")

canvas.create_text(
    57.0,
    450.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    0.0,
    473.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("TruculentaRoman Regular", 40 * -1)
)

button_image_4 = PhotoImage(
    file="button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=544.0,
    y=473.0,
    width=124.0,
    height=44.0
)

button_image_hover_4 = PhotoImage(
    file="button_hover_5.png")

def button_4_hover(e):
    button_4.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    button_4.config(
        image=button_image_4
    )

button_4.bind('<Enter>', button_4_hover)
button_4.bind('<Leave>', button_4_leave)


canvas.create_rectangle(
    777.0,
    450.0,
    1253.0,
    553.0,
    fill="#000000",
    outline="")

canvas.create_text(
    777.0,
    453.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    720.0,
    476.0,
    anchor="nw",
    text="D",
    fill="#FFFFFF",
    font=("TruculentaRoman Regular", 40 * -1)
)

button_image_5 = PhotoImage(
    file="button_5.png")
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=1264.0,
    y=476.0,
    width=124.0,
    height=44.0
)

button_image_hover_5 = PhotoImage(
    file="button_hover_6.png")

def button_5_hover(e):
    button_5.config(
        image=button_image_hover_5
    )
def button_5_leave(e):
    button_5.config(
        image=button_image_5
    )

button_5.bind('<Enter>', button_5_hover)
button_5.bind('<Leave>', button_5_leave)


canvas.create_text(
    777.0,
    233.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    720.0,
    256.0,
    anchor="nw",
    text="B",
    fill="#FFFFFF",
    font=("TruculentaRoman Regular", 40 * -1)
)

button_image_6 = PhotoImage(
    file="button_6.png")
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1264.0,
    y=256.0,
    width=124.0,
    height=44.0
)

button_image_hover_6 = PhotoImage(
    file="button_hover_7.png")

def button_6_hover(e):
    button_6.config(
        image=button_image_hover_6
    )
def button_6_leave(e):
    button_6.config(
        image=button_image_6
    )

button_6.bind('<Enter>', button_6_hover)
button_6.bind('<Leave>', button_6_leave)

window.resizable(True, True)
window.mainloop()
