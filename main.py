#pip3 install -r requirements.txt
from PIL import Image
import os
import sqlite3
import json

from customtkinter import *

from globall import *
def add_city(name):# Добавляем новый город в базу данных
    site.execute("INSERT INTO cities (name) VALUES (?)", (name,))
    site.commit()
def add_city_opis(name, description, location):
    # Добавляем новый город описание в базу данных
    opisenie_cursor.execute("INSERT INTO cities (name, description, location) VALUES (?, ?, ?)", (name, description, location))
def check_city(name):# Проверяем наличие города в базе данных
    cursor = site.execute("SELECT name FROM cities WHERE name=?", (name,))
    city = cursor.fetchone()
    if city:
        return 1
    else:
        return 0
def add_user(login, password, array1, array2):
    array1_join = json.dumps(array1)
    array2_join = json.dumps(array2)
    c.execute("INSERT INTO users (login, password, array1, array2) VALUES (?, ?, ?, ?)",
              (login, password, array1_join, array2_join))
    conn.commit()
def get_users():
    c.execute('SELECT * FROM users')
    rows = c.fetchall()
    for row in rows:
        print(row)
def delete_user(login):
    c.execute('DELETE FROM users WHERE login=?', (login,))
    conn.commit()
def read_login_pasvord():
    c.execute(f'SELECT login,password FROM users')
    rows = c.fetchall()
    return rows
def read_negativ(login):
    c.execute(f'SELECT array1 FROM users WHERE login=?', (login,))
    rows = c.fetchall()
    rows = list(rows[0])
    return rows
def read_pozitive(login):
    c.execute(f'SELECT array2 FROM users WHERE login=?', (login,))
    rows = c.fetchall()
    rows = list(rows[0])
    return rows
def read_all(login):
    return (read_negativ(login)[0][1:-1]).split(", ")+(read_pozitive(login)[0][1:-1]).split(", ")


conn = sqlite3.connect('file(sgl)/database.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              login TEXT,
              password TEXT,
              array1 TEXT,
              array2 TEXT
    )
''')
site = sqlite3.connect('file(sgl)/cities.db')
site.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL);''')
opisenie = sqlite3.connect('file(sgl)/opisenie.db')
opisenie_cursor = opisenie.cursor()
opisenie_cursor.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             description TEXT NOT NULL,
             location TEXT NOT NULL);''')
# add_city_opis("Санкт-Петербург", "Город на Неве", "Северо-Западная Россия")
# opisenie.commit()
set_appearance_mode("light")
set_default_color_theme("dark-blue")
#print((read_negativ("фывывфывфывф")[0][1:-1]).replace(' ', '').split(','))
class App(CTk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "test_images")
        self.logo_image = CTkImage(Image.open(
            os.path.join(image_path, "CustomTkinter_logo_single.png")),
            size=(26, 26))
        self.home_image = CTkImage(light_image=Image.open(
            os.path.join(image_path, "home_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "home_light.png")),
            size=(20, 20))
        self.chat_image = CTkImage(light_image=Image.open(
            os.path.join(image_path, "chat_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
            size=(20, 20))
        self.add_user_image = CTkImage(
            light_image=Image.open(os.path.join(image_path,
                                "add_user_dark.png")),
            dark_image=Image.open(
            os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.galochka_image = CTkImage(light_image=Image.open(
            os.path.join(image_path, "mark_blake.png")),
            dark_image=Image.open(os.path.join(image_path,
                                "mark_white.png")),
            size=(20, 20))
        self.plase_image = CTkImage(light_image=Image.open(
            os.path.join(image_path, "900364.png")),
            dark_image=Image.open(os.path.join(image_path, "900364_white.png")),
            size=(20, 20))

        p = open('file(sgl)/Логин', 'r', encoding="UTF-8")
        self.login_frame = CTkFrame(self)
        self.login_label = CTkLabel(self.login_frame,
            text="Регистрация/Вход",
            font=CTkFont(size=30, weight="bold"))
        self.title("Богадство мира")
        if p.read() == '':
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.after(0, lambda: self.state('zoomed'))

            self.login_frame.grid(row=0, column=0, padx=20, pady=20
            , sticky="nsew")
            self.login_label.grid(row=0, column=0,
            padx=screen_width//2 - 160, pady=(150, 15))
            self.username_entry = CTkEntry(self.login_frame,
            width=200, placeholder_text="Логин",)
            self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
            self.password_entry = CTkEntry(self.login_frame,
            width=200, show="*", placeholder_text="Пароль")
            self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
            self.login_button = CTkButton(self.login_frame
            , text="Войти", command=self.main, width=200)
            self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        else:
            self.main()
        p.close()
    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25")
        if name == FRAMGL_NAME else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25")
        if name == FRAM1_NAME else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25")
        if name == FRAM2_NAME else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25")
        if name == FRAM3_NAME else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25")
        if name == FRAM4_NAME else "transparent")
        # Показ выбранного
        if name == FRAMGL_NAME:
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == FRAM2_NAME:
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == FRAM1_NAME:
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == FRAM3_NAME:
            self.negative_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.negative_frame.grid_forget()
        if name == FRAM4_NAME:
            self.pozitive_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.pozitive_frame.grid_forget()
    def home_button_event(self):self.select_frame_by_name(FRAMGL_NAME)
    def frame_2_button_event(self):self.select_frame_by_name(FRAM1_NAME)
    def frame_3_button_event(self):self.select_frame_by_name(FRAM2_NAME)
    def frame_4_button_event(self):self.select_frame_by_name(FRAM3_NAME)
    def frame_5_button_event(self):self.select_frame_by_name(FRAM4_NAME)
    def main(self):
        if self.login_event():
            return
        self.login_label.destroy()
        self.login_frame.destroy()
        self.after(0, lambda:self.state('zoomed'))
        self.pozitive = (read_negativ("фывывфывфывф")[0][1:-1]).replace(' ', '').split(',')
        # установиливаю макет сетки 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # Навигация
        self.navigation_frame = CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)
        self.navigation_frame_label = CTkLabel(
                self.navigation_frame,
                text="  Image Example",
                image=self.logo_image, compound="left",
                font=CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        # 1 фрейм
        self.home_button = CTkButton(self.navigation_frame,
                corner_radius=0,
                height=40, border_spacing=10,
                text=FRAMGL_NAME,
                fg_color="transparent", text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                image=self.home_image, anchor="w",
                command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        # 2 фрейм
        self.frame_2_button = CTkButton(self.navigation_frame,
                corner_radius=0, height=40,
                border_spacing=10, text=FRAM1_NAME, fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"), image=self.chat_image,
                anchor="w",
                command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        # 3 фрейм
        self.frame_3_button = CTkButton(
                self.navigation_frame, corner_radius=0, height=40,
                border_spacing=10, text=FRAM2_NAME,
                fg_color="transparent", text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                image=self.add_user_image, anchor="w",
                command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        # 4 фрейм
        self.frame_4_button = CTkButton(
            self.navigation_frame, corner_radius=0, height=40,
            border_spacing=10, text=FRAM3_NAME,
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.galochka_image, anchor="w",
            command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")
        # 5 фрейм
        self.frame_5_button = CTkButton(
            self.navigation_frame, corner_radius=0, height=40,
            border_spacing=10, text=FRAM4_NAME,
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.plase_image, anchor="w",
            command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")
        # выбор темы
        self.appearance_mode_menu = CTkOptionMenu(
                self.navigation_frame,
                values=["Светлая", "Тёмная", "Системная"],
                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6,
                column=0, padx=20, pady=20, sticky="s")

        # Главный фрейм
        self.home_frame = CTkFrame(self,
                corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        screen_height = self.winfo_screenheight()

        self.home_Lable = CTkLabel(self.home_frame,
        text='Главная', font=CTkFont(size=40, weight="bold"))
        self.home_Lable.grid()

        self.home_None = CTkLabel(self.home_frame,
        text='',)
        self.home_None.grid(row=1, column=0)
        self.home_None = CTkLabel(self.home_frame,
                                                text='', )
        self.home_None.grid(row=2, column=0)
        self.home_None = CTkLabel(self.home_frame,
                                                text='', )
        self.home_None.grid(row=3, column=0)

        self.home_Lable_all = CTkLabel(self.home_frame,
        text='Город            Название'
             '              Описание                 Уже был       '
             '             Не хочу быть',
            font=CTkFont(size=30, weight="bold"))
        self.home_Lable_all.grid(row=4, column=0)

        tk_textbox = CTkScrollableFrame(self.home_frame,
                                height=screen_height-250)
        tk_textbox.grid(row=5, column=0, sticky="nsew")
        tk_textbox.grid_columnconfigure(0, weight=1)
        tk_textbox.grid_columnconfigure(1, weight=1)
        tk_textbox.grid_columnconfigure(2, weight=1)
        tk_textbox.grid_columnconfigure(3, weight=1)
        tk_textbox.grid_columnconfigure(4, weight=1)
        self.home_masive_install(tk_textbox)

        # создаем 3 фрейм
        self.second_frame = CTkFrame(self, corner_radius=0,
            fg_color="transparent")
        # Настройка
        self.navigation_frame2_label = CTkLabel(
                self.second_frame,
                text=LOGIN,
                font=CTkFont(size=30, weight="bold"))
        self.navigation_frame2_label.grid(padx=200, pady=100)
        # создаем 2 фрейм
        self.third_frame = CTkFrame(self, corner_radius=0,
            fg_color="transparent")
        # создаём 4 фрейм
        self.negative_frame = CTkFrame(self, corner_radius=0,
                                                   fg_color="transparent")
        # создаём 5 фрейм
        self.pozitive_frame = CTkFrame(self, corner_radius=0,
                                                fg_color="transparent")
        # Настройка
        self.navigation_frame_label = CTkLabel(self.third_frame,
        text="Введите название достопремечательности и через / описание",
        font=CTkFont(size=30, weight="bold"))
        self.navigation_frame_label.grid(padx=200, pady=100)
        self.home_frame_frame_2_entry = CTkEntry(
            self.third_frame, width=1000, height=50)
        self.home_frame_frame_2_entry.grid(row=1, column=0,
                                    padx=200, pady=10, sticky="nsw")
        self.bitin_2frame = CTkButton(self.third_frame
            , text='Отправить на проверку', height=50)
        self.bitin_2frame.grid(row=2, column=0, padx=200, pady=10)
        # Главный фрейм
        self.select_frame_by_name(FRAMGL_NAME)
    def home_masive_install(self,sel):
        global LOGIN
        p = open('file(sgl)/Логин', 'r', encoding="UTF-8")
        LOGIN = p.read()
        opisenie_cursor.execute("SELECT name, description, location FROM cities")
        rows = opisenie_cursor.fetchall()
        f = 0
        for _ in rows:
            f += 1
        self.home_masive = []
        self.mas = [1,2,3,4,5,6]
        for i in range(f):
            self.home_masive.append(self.mas)
            opisenie_cursor.execute('SELECT name,description,location FROM cities')
            rows = opisenie_cursor.fetchall()
            for row in rows:
                self.home_masive[i][0] = CTkLabel(sel, text=row[0])
                self.home_masive[i][1] = CTkLabel(sel, text=row[1])
                self.home_masive[i][2] = CTkLabel(sel, text=row[2])
                self.home_masive[i][3] = CTkButton(sel, text='Уже был', command=self.biton_pozitive)
                self.home_masive[i][4] = CTkButton(sel, text='Не хочу', command=self.biton_negetive)
        self.home_masive_grid(f)
    def biton_pozitive(self):
        self.home_masive_delite()
        self.pozitive+=L# где взять L
        c.execute(f'UPDATE users SET array1 = ? WHERE login = ?', (self.pozitive, LOGIN))
        c.commit()

        self.home_masive_grid()
    def biton_negetive(self):
        ...
    def home_masive_grid(self, f):
        for i in range(f):
            if str(i+1) not in read_all(LOGIN):
                self.home_masive[i][0].grid(row=i, column=0)
                self.home_masive[i][1].grid(row=i, column=1)
                self.home_masive[i][2].grid(row=i, column=2)
                self.home_masive[i][3].grid(row=i, column=3)
                self.home_masive[i][4].grid(row=i, column=4)
    def home_masive_delite(self, sel):
        for i in range(f):
            if str(i) not in read_all(LOGIN):
                sel.home_masive.append(sel.mas)
                sel.home_masive[i][0].destroy()
                sel.home_masive[i][1].destroy()
                sel.home_masive[i][2].destroy()
                sel.home_masive[i][3].destroy()
                sel.home_masive[i][4].destroy()
    @staticmethod
    def change_appearance_mode_event(new_appearance_mode):
        if new_appearance_mode == 'Светлая':
            set_appearance_mode("light")
        elif new_appearance_mode == 'Тёмная':
            set_appearance_mode("dark")
        else:
            set_appearance_mode("system")
    def avtor(self, password):
        if password == '':
            return 1
        if LOGIN == '':
            return 1

        for file3 in read_login_pasvord():
            if file3[0] == LOGIN:
                if file3[1] == password:
                    p = open('file(sgl)/Логин', 'w', encoding="UTF-8")
                    p.write(LOGIN)
                    p.close()
                    self.login_frame.grid_forget()
                    self.login_frame.grid(row=0, column=0, sticky="nsew", padx=100)
                    return 0
                else:
                    self.login_label1.grid_forget()
                    self.login_label1 = CTkLabel(
                        self.login_frame, text="Пароль или логин\nне правильный",
                        font=CTkFont(size=20, weight="bold"))
                    self.login_label1.grid(row=4, column=0)
                    return 1
        add_user(LOGIN, password,[0],[0])
        p = open('file(sgl)/Логин', 'w', encoding="UTF-8")
        p.write(LOGIN)
        self.login_label1.grid_forget()
        p.close()
        return 0
    def login_event(self):
        global LOGIN
        self.login_label1 = CTkLabel(self.login_frame
            , text="",
             font=CTkFont(size=20, weight="bold"))
        self.login_label1.grid(row=4, column=0)
        p = open('file(sgl)/Логин', 'r', encoding="UTF-8")
        if p.read() == '':
            LOGIN = self.username_entry.get()
            password = self.password_entry.get()
        else:
            LOGIN = p.read()
            return 0
        p.close()
        return self.avtor(password)

if __name__ == "__main__":
    app = App()
    app.mainloop()
    conn.close()
    site.close()
    opisenie.close()
