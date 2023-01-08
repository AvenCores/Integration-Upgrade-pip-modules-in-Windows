from tkinter import Tk,Canvas,PhotoImage,messagebox,Button,Label,CENTER
from requests import get
from os import system

root = Tk()
root.title('HZF pyupgrade install')
root.geometry('300x250')
root.resizable(width=False, height=False)

f=open(r'pylogo.png', "wb")
ufr = get("https://i.imgur.com/HG0sFE0.png")
f.write(ufr.content)
f.close()

canvas = Canvas(root, height=400, width=400)
canvas.pack()
logoimg = PhotoImage(file='pylogo.png')
renderImg = canvas.create_image(150,75, image=logoimg)

def installupgr():
    system("del /Q pyupgrade.py")
    f=open(r'pyupgrade.py', "wb")
    ufr = get("https://pastebin.com/raw/8gX3heGA")
    f.write(ufr.content)
    f.close()

    f=open(r'install.bat', "wb")
    ufr = get("https://pastebin.com/raw/iPLmJ7ws")
    f.write(ufr.content)
    f.close()
    system('install.bat')
    system('del /Q install.bat')
    system('del /Q pyupgrade.py')
    messagebox.showinfo(title="Установлено!", message='Pyupgrade был успешно установлен.')

def remupgr():
    system('del /Q %USERPROFILE%\AppData\Local\Programs\Python\Python311\Scripts\pyupgrade.py')
    messagebox.showinfo(title="Удалено!", message='Pyupgrade был успешно удален.')

inst = Button(text='Установить скрипт', command=installupgr)
inst.place(x=100, y=140)

rem = Button(text='Удалить скрипт', command=remupgr)
rem.place(x=100, y=180)

poetry = 't.me/hzfnews'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=5, y=225)

root.mainloop()
system("del /Q pyupgrade.py")
system("del /Q pylogo.png")