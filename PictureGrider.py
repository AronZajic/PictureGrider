from tkinter import Tk, Canvas, Button, filedialog, Spinbox, StringVar
from PIL import ImageTk,Image

root = Tk()

root.state('zoomed')

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())

img = None
h = None
w = None
sh = 80
sw = 50

def loading():

    global img, h, w

    s = str(filedialog.askopenfile(mode='r').name)

    image = Image.open(s)

    h = root.winfo_screenheight() - sh
    w = root.winfo_screenwidth() - sw

    if h / image.height > w / image.width:
        image = image.resize((int(image.width * (w / image.width)), int(image.height *
                              (w / image.width))), Image.ANTIALIAS)
    else:
        image = image.resize((int(image.width * (h / image.height)), int(image.height *
                              (h / image.height))), Image.ANTIALIAS)
    
    img = ImageTk.PhotoImage(image)

    mriezkuj(None)

load = Button(root, text ="Load", command = loading)
load.place(x = 5, y = 5)

xo = StringVar()
xo.set('')

xbut = Spinbox(root, from_ = 0, to = 1000, increment = 1, textvariable=xo, width = 3)
xbut.place(x = 5, y = 35)

yo = StringVar()
yo.set('')

ybut = Spinbox(root, from_ = 0, to = 1000, increment = 1, textvariable=yo, width = 3)
ybut.place(x = 5, y = 60)

def mriezkuj(*args):
    global img

    canvas.delete("all")

    for ix in range(1, 100):
        if ix % 10 == 0:
            canvas.create_text(sw + ix * (w / 100), 30, text = str(ix)[0], font="Times 20 bold")
            canvas.create_line(sw + ix * (w / 100), 50, sw + ix * (w / 100), 100, fill='red')
        else:
            canvas.create_line(sw + ix * (w / 100), 70, sw + ix * (w / 100), 100, fill='red')

    for iy in range(1, 100):
        if iy % 10 == 0:
            canvas.create_text(10, sh + iy * (w / 100),text = str(iy)[0], font="Times 20 bold")
            canvas.create_line(20, sh + iy * (w / 100), 50, sh + iy * (w / 100),fill='red')
        else:
            canvas.create_line(40, sh + iy * (w / 100), 50, sh + iy * (w / 100),fill='red')

    canvas.create_image(sw, sh, image=img, anchor="nw")
    
    if img is not None:
        iy = sh + img.width() / (int(yo.get()) + 1)
        while iy < sh + img.height():
            canvas.create_line(sw, iy, root.winfo_screenwidth(), iy, fill='red')
            iy += img.width() / (int(yo.get()) + 1)

        ix = sw + img.width() / (int(xo.get()) + 1)
        while ix < sw + img.width():
            canvas.create_line(ix, sh, ix, root.winfo_screenheight(), fill='red')
            ix += img.width() / (int(xo.get()) + 1)

yo.trace("w", mriezkuj)
xo.trace("w", mriezkuj)

loading()

canvas.pack()

root.mainloop()
