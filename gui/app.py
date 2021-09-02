
from tkinter import *


def run():
    root = Tk()
    root.title('Bas Creator')
    root.geometry('800x600')  # 这里的乘号不是 * ，而是小写英文字母 x

    txt = Text(root)
    txt.grid(column=0, rowspan=10)
    createRadioBox(root)

    Label(root, text='弹幕开始时间（秒）').grid(column=1, columnspan=3, row=1)
    inp1 = Entry(root)
    inp1.grid(column=1, columnspan=3, row=2)

    root.mainloop()


def createRadioBox(root):
    var = IntVar()
    rd1 = Radiobutton(root, text="Text", variable=var,
                      value=0, command=onRadioButton)
    rd1.grid(column=1, row=0)

    rd2 = Radiobutton(root, text="Path", variable=var,
                      value=1, command=onRadioButton)
    rd2.grid(column=2, row=0)

    rd3 = Radiobutton(root, text="SVG", variable=var,
                      value=2, command=onRadioButton)
    rd3.grid(column=3, row=0)


def onRadioButton(var):
    print(var.get())
