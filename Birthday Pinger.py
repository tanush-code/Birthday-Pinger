import pandas as p
import datetime
import webbrowser
import pyautogui
import time
from tkinter import *
root = Tk()
root.title("Birthday reminder")
root.maxsize(width=80,height=80)

def wishthemininsta():
    webbrowser.open('www.instagram.com/' + item['insta id'])
    time.sleep(8)
    pyautogui.moveTo(760, 170)
    pyautogui.click()
    time.sleep(3)
    pyautogui.write(item['wish'])
    pyautogui.press('enter')
def check_birthday():
    br = p.read_excel("Birthday.xlsx")
    today = datetime.datetime.now().strftime('%d-%m')
    # print(today)
    global item
    for index, item in br.iterrows():
        # print(index, item['date'])
        birthday_date = item['date'].strftime('%d-%m')
        name = item['name']
        # print(name)
    if item['date'] in today:
        main = Tk()
        main.maxsize()
        main.title("Wish them")
        photo =PhotoImage(file='plswork.png')
        plsphoto = Label(root,text=photo).pack()
        name = Label(main,text = "today is the birthday of " + item['name'] + " should I wish her",font='arial')
        name.pack()
        button2 = Button(main,text="wish her",relief=SUNKEN,fg="red",font='arial',command=wishthemininsta).pack()
        main.mainloop()
    else:
        maina = Tk()
        last = Label(maina,text="No Birthday Today",fg="red",font=('bold')).pack()
        maina.mainloop()
button1 = Button(root,text="Check for birthday",relief=SUNKEN,fg="red",font='arial',command=check_birthday)
button1.pack()
button2 = Button(root,text="Quit",relief=SUNKEN,fg="red",font='arial',command=quit).pack()
root.mainloop()