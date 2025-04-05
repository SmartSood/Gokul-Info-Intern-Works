
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/smarthsood/Desktop/APP4_updated_gui/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x832")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1274.0,
    832.0,
    fill="#063C53",
    outline="")

canvas.create_rectangle(
    57.0,
    17.0,
    1003.0,
    149.0,
    fill="#FFFCFC",
    outline="")

canvas.create_text(
    57.0,
    17.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_rectangle(
    53.0,
    171.0,
    499.0,
    274.0,
    fill="#000000",
    outline="")

canvas.create_text(
    53.0,
    174.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    0.0,
    197.0,
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
    x=509.7964172363281,
    y=199.0,
    width=116.2035903930664,
    height=44.0
)

canvas.create_rectangle(
    173.0,
    582.0,
    1134.0,
    733.0,
    fill="#000000",
    outline="")

canvas.create_text(
    173.0,
    582.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    0.0,
    629.0,
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
    x=1143.0,
    y=636.0,
    width=124.0,
    height=44.0
)

canvas.create_rectangle(
    343.0,
    450.0,
    819.0,
    553.0,
    fill="#000000",
    outline="")

canvas.create_text(
    343.0,
    453.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    169.0,
    476.0,
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
    x=830.0,
    y=476.0,
    width=124.0,
    height=44.0
)
/Users/smarthsood/Desktop/APP4_updated_gui/build/button_7.png /Users/smarthsood/Desktop/APP4_updated_gui/build/button_8.png /Users/smarthsood/Desktop/APP4_updated_gui/build/button_9.png /Users/smarthsood/Desktop/APP4_updated_gui/build/button_10.png
canvas.create_rectangle(
    658.0,
    165.0,
    1134.0,
    268.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    53.0,
    318.0,
    494.0,
    421.0,
    fill="#000000",
    outline="")

canvas.create_text(
    53.0,
    321.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    0.0,
    344.0,
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
    x=504.0957946777344,
    y=344.0,
    width=114.90419006347656,
    height=44.0
)

canvas.create_rectangle(
    655.0,
    314.0,
    1138.0,
    417.0,
    fill="#000000",
    outline="")

canvas.create_text(
    655.0,
    317.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    618.0,
    340.0,
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
    x=1143.0,
    y=340.0,
    width=118.61676788330078,
    height=44.0
)

canvas.create_text(
    658.0,
    168.0,
    anchor="nw",
    text="LOREM %)",
    fill="#000000",
    font=("TruculentaRoman Regular", 40 * -1)
)

canvas.create_text(
    619.0,
    191.0,
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
    x=1138.0,
    y=191.0,
    width=124.0,
    height=44.0
)

button_image_7 = PhotoImage(
    file="button_7.png")
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=1140.0,
    y=56.0,
    width=124.0,
    height=44.0
)

button_image_8 = PhotoImage(
    file="button_8.png")
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=1053.0,
    y=752.0,
    width=211.0,
    height=44.0
)

button_image_9 = PhotoImage(
    file="button_9.png")
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=263.0,
    y=752.0,
    width=211.0,
    height=44.0
)

button_image_10 = PhotoImage(
    file="button_10.png")
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=22.0,
    y=752.0,
    width=211.0,
    height=44.0
)

canvas.create_rectangle(
    24.0,
    28.0,
    124.0,
    128.0,
    fill="#000000",
    outline="")
window.resizable(True, True)
window.mainloop()
