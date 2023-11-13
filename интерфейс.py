from tkinter import *
from tkinter import ttk

h = 0
color = str(1234) + 'ff'


def interfey():
    ...


def delite():  # удаление окна и возможность открытия нового
    global h
    h = 0
    root1.destroy()


def avtor(login, password, g):  # Авторизация/Вход
    file = open('Авторизация', 'a', encoding="UTF-8")
    for file3 in open('Авторизация', 'r', encoding="UTF-8"):
        if file3[2:file3.find('\t', 2)] == login:
            if file3[file3.find('\t', 2) + 1:file3.find('\t', file3.find('\t', 2) + 1)] == password:
                text['text'] = 'Вы вошли'
                btit.destroy()
                p = open('Логин', 'w', encoding="UTF-8")
                p.write(login)
                p.close()
                root1.destroy()
                return
            else:
                text['text'] = 'Пароль не правильный'
                return
    file.write(str(int(g) + 1) + '\t' + login + '\t' + password + '\t' + 'f' + '\n')
    file.close()
    p = open('Логин', 'w', encoding="UTF-8")
    p.write(login)
    text['text'] = "Пользователь создан"
    btit.destroy()
    root1.destroy()
    p.close()
    return


def btn_clic():  # Проверка пользователя
    login = loginInput.get()
    password = passwordInput.get()
    if login == '' and password == '':
        text['text'] = 'Нет логина и пароля'
    elif login == '':
        text['text'] = 'Нет логина'
    elif password == '':
        text['text'] = 'Нет пароля'
    else:
        g = 0
        for nine in open('Авторизация', 'r', encoding="UTF-8"):
            if nine != '':
                g = nine[0]
            if g == 'Л':
                g = 0
        if login.count('\t'):
            text['text'] = "Логин болжен быть без таба "
            text.pack()
            return
        if password.count('\t'):
            text['text'] = "Пароль болжен быть без таба "
            text.pack()
            return
        avtor(login, password, g)
    return


def btn():  # Создание 2 окна
    # Регистрация
    global loginInput, passwordInput, text, root1, h
    if h == 0:
        root1 = Toplevel()
        h = 1
        screen_width = root1.winfo_screenwidth()  # длина
        screen_height = root1.winfo_screenheight()  # высота экрана
        root1.protocol("WM_DELETE_WINDOW", delite)  # Проверка на закрытие
        root1['bg'] = f'#{color}'
        root1.title('Название программы')
        root1.geometry(f'{screen_width // 5}x{screen_height // 2}')  # размер и цвет экрана

        logi = Label(root1, text='Логин')  # текст
        logi.pack()

        loginInput = ttk.Entry(root1, background='white')  # поле ввода
        loginInput.pack()

        passwor = Label(root1, text='Пароль')  # текст
        passwor.pack()

        passwordInput = ttk.Entry(root1, background='white')  # поле ввода
        passwordInput.pack()
        text = ttk.Label(root1, text='120')
        bt = ttk.Button(root1, text='Проверка', command=btn_clic)  # кнопка
        bt.pack()

        root1.mainloop()


root = Tk()

root['bg'] = f'#{color}'
root.title('Название программы')
root.geometry(f'{600}x{700}')

btit = ttk.Button(root, text='Зарегестрироватся/Войти', command=btn)
lo = open('Логин', 'r', encoding="UTF-8")

if lo.read() == '':
    btit.pack()
else:
    ...

root.mainloop()
