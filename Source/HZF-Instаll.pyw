from tkinter import Tk,Canvas,PhotoImage,messagebox,Button,Label,CENTER,Menu
from requests import get
from os import system
from sys import platform
import ctypes as ct
import webbrowser

version = "3.2"

if platform == "win32":
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

    canvas = Canvas(root, bg="#000000", width=100, height=120)
    canvas.pack()
    logoimg = PhotoImage(file='pylogo.png')
    canvas.create_image(53,75, image=logoimg)

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

    def opentgchannel():
        url = "https://t.me/hzfnews"
        webbrowser.open(url, new=2)

    def openytchannel():
        url = "https://www.youtube.com/c/HZFYT"
        webbrowser.open(url, new=2)

    def opendiscord():
        url = "https://discord.com/invite/7bneGfUS5h"
        webbrowser.open(url, new=2)

    def openvkgroup():
        url = "https://vk.com/hzforum1"
        webbrowser.open(url, new=2)

    def devtgopen():
        url = "https://t.me/avencores"
        webbrowser.open(url, new=2)

    def qiwi():
        url = "http://qiwi.com/n/AVENCORESDONATE"
        webbrowser.open(url, new=2)

    def cber():
        messagebox.showinfo(title="Сбер Донат", message="2202 2050 7215 4401")

    def vtb():
        messagebox.showinfo(title="ВТБ Донат", message="2200 2404 1001 8580")

    def omyprog():
        messagebox.showinfo(title="О программе", message=f"""Integration Upgrade pip modules - это скрипт от команды HZF, который поможет обновить все установленные pip модули в системе в один клик! 

Автор утилиты: avencores

Интерфейс: Tkinter

Версия: {version}
    """)

    mainmenu = Menu(root) 
    root.config(menu=mainmenu)  

    mygroup = Menu(mainmenu, tearoff=0)
    mygroup.add_command(label="Telegram Channel", command=opentgchannel)
    mygroup.add_command(label="YouTube Channel", command=openytchannel)
    mygroup.add_command(label="Discord Channel", command=opendiscord)
    mygroup.add_command(label="VK Group", command=openvkgroup)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="Написать разработчику", command=devtgopen)
    helpmenu.add_separator()  
    helpmenu.add_command(label="О программе", command=omyprog)

    donatemenu = Menu(mainmenu, tearoff=0)
    donatemenu.add_command(label="Qiwi Донат", command=qiwi)
    donatemenu.add_command(label="Сбер Донат", command=cber)
    donatemenu.add_command(label="ВТБ Донат", command=vtb)

    mainmenu.add_cascade(label="Информация", menu=mygroup)
    mainmenu.add_cascade(label="Донат", menu=donatemenu)
    mainmenu.add_cascade(label="Справка", menu=helpmenu)

    root.deiconify()
    root.mainloop()
    system("del /Q pyupgrade.py")
    system("del /Q pylogo.png")

elif platform == "linux" or platform == "linux2" or platform == "unix":
    messagebox.showerror(title="Unsupported system", message="Ваша система не поддерживается!")