from tkinter import *
from tkinter import ttk


def btn_clic():
    login = loginInput.get()
    password = passwordInput.get()
    if login == '' and password == '':
        print('Нет логина и пароля')
    elif login == '':
        print('Нет логина')
    elif password == '':
        print('Нет пароля')
    else:
        print(login, password)


root = Tk()

screen_width = root.winfo_screenwidth()  # длина
screen_height = root.winfo_screenheight()  # высота экрана

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH, side=LEFT)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)

notebook.add(frame1, text='1')
notebook.add(frame2, text='2')
notebook.add(frame3, text='3')
notebook.add(frame4, text='4')

root['bg'] = '#fafafa'
root.title('Название программы')
root.geometry(f'{screen_width}x{screen_height}')

title = ttk.Label(frame1, text='Подсказка', background='gray')
title.pack()

btn = ttk.Button(frame1, text='Кнопка', command=btn_clic)
btn.pack()

loginInput = ttk.Entry(frame1, background='white')
loginInput.pack()

passwordInput = ttk.Entry(frame1, background='white')
passwordInput.pack()

root.mainloop()
