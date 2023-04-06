from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1500x800")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 800,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    756.0, 431.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    1176.0, 441.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f9f3f3",
    highlightthickness = 0)

entry0.place(
    x = 1051, y = 429,
    width = 250,
    height = 23)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    1176.0, 553.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#fffbfb",
    highlightthickness = 0)

entry1.place(
    x = 1051, y = 541,
    width = 250,
    height = 23)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 1081, y = 600,
    width = 141,
    height = 45)

window.resizable(True, True)
window.mainloop()
