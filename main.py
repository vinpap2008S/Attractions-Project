# pip install -r requirements.txt
from PIL import Image
import os
import sqlite3
import json

import tkinter
from customtkinter import *

from globall import *
def add_city(name):# Добавляем новый город в базу данных
    site.execute("INSERT INTO cities (name) VALUES (?)", (name,))
    site.commit()
def add_city_opis(name, description, location, vid):
    # Добавляем новый город описание в базу данных
    opisenie_cursor.execute("INSERT INTO cities (name, description, location, vid)"
                            " VALUES (?, ?, ?, ?)", (name, description, location, vid))
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
    c.execute(f'SELECT array2 FROM users WHERE login=?', (login,))
    rows = c.fetchall()
    rows = json.loads(rows[0][0])
    return rows
def read_pozitive(login):
    c.execute(f'SELECT array1 FROM users WHERE login=?', (login,))
    rows = c.fetchall()
    rows = json.loads(rows[0][0])
    return rows
def read_all(login):
    a = list(read_negativ(login)+read_pozitive(login))
    a.sort()
    return a
def len_txt(txt, minys):
    if len(txt) <= minys:
        return ((len(txt)-minys)//2 + (len(txt)-minys)%2)*''+txt+' '*((len(txt)-minys)//2)
    else:
        return txt[:minys-3] + "..."
conn = sqlite3.connect('file(sgl)/database.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              login TEXT NOT NULL,
              password TEXT NOT NULL,
              array1 TEXT NOT NULL,
              array2 TEXT NOT NULL
    )
''')
site = sqlite3.connect('file(sgl)/cities.db')
sit = site.cursor()
sit.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL);''')
sit.execute('SELECT name FROM cities')
rowsh = sit.fetchall()
opisenie = sqlite3.connect('file(sgl)/opisenie.db')
opisenie_cursor = opisenie.cursor()
opisenie_cursor.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             description TEXT NOT NULL,
             location TEXT NOT NULL,
             vid TEXT NOT NULL);''')
set_appearance_mode("light")
set_default_color_theme("dark-blue")

class App(CTk):
    def __init__(self):
        super().__init__()
        self.cites_poisk = ""
        self.name_poisk = ""
        self.vid_poisk = ""
        self.toplevel_window = None
        screen_width = self.winfo_screenwidth()
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "test_images")
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
            os.path.join(image_path, "free-icon-checked-153603.png")),
            dark_image=Image.open(os.path.join(image_path,
                                "free-icon-checked-153603 (1).png")),
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
        self.title("Богатство мира")
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
            self.pozitive_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.pozitive_frame.grid_forget()
        if name == FRAM4_NAME:
            self.negative_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.negative_frame.grid_forget()
    def home_button_event(self):self.select_frame_by_name(FRAMGL_NAME)
    def frame_2_button_event(self):self.select_frame_by_name(FRAM1_NAME)
    def frame_3_button_event(self):self.select_frame_by_name(FRAM2_NAME)
    def frame_4_button_event(self):self.select_frame_by_name(FRAM3_NAME)
    def frame_5_button_event(self):self.select_frame_by_name(FRAM4_NAME)
    def poisk_cite(self):
        self.poi = self.home_frame__entry2.get()
        if self.poi != "":
            self.poi = self.poi[0].upper() + self.poi[1:].lower()
        self.home_frame_entry.configure(
            values=["Город"] + [i[0] for i in rowsh if (self.poi in i[0]) or self.poi == ''])
    def poisk_all(self):
        self.cites_poisk = self.home_frame_entry.get() if(
                self.home_frame_entry.get() != "Город"
                and self.home_frame_entry.get() is not None) else ""
        self.name_poisk = self.home_frame_entry_name.get()\
            if self.home_frame_entry_name.get() is not None else ""
        self.vid_poisk = self.home_frame_entry_vid.get() if (
                self.home_frame_entry_vid.get() != "Вид" and
                self.home_frame_entry_vid.get() is not None)else ""
        self.home_masive_delite(f)
        self.home_masive_install()
    def main(self):
        if self.login_event():
            return
        self.login_label.destroy()
        self.login_frame.destroy()
        self.poisk = ''
        self.after(0, lambda:self.state('zoomed'))
        p = open('file(sgl)/Логин', 'r', encoding="UTF-8")
        LOGIN = p.read()
        p.close()
        self.pozitive = read_pozitive(LOGIN)
        self.negative = read_negativ(LOGIN)
        # установиливаю макет сетки 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # Навигация
        self.navigation_frame = CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)
        self.navigation_frame_label = CTkLabel(
                self.navigation_frame,
                text="Богатство мира",compound="left",
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
        self.home_Lable.grid(columnspan=10)

        self.home_None = CTkLabel(self.home_frame,
        text='',)
        self.home_None.grid(row=1, columnspan=10)
        self.home_None = CTkLabel(self.home_frame,
                                                text='', )
        self.home_None.grid(row=2, columnspan=10)
        self.home_None = CTkLabel(self.home_frame,
                                                text='', )
        self.home_None.grid(row=3, columnspan=10)
        self.home_frame.grid_columnconfigure([0,1,2,3,4,5], weight=1)


        self.home_frame__entry2 = CTkEntry(
            self.home_frame, placeholder_text="Название города", width=200, height=50)
        self.home_frame__entry2.grid(row=4, column=0,
                                            padx=10, pady=10, sticky="nsw")

        self.home_frame_entry2_buton = CTkButton(self.home_frame, text="Поиск города", command=self.poisk_cite)
        self.home_frame_entry2_buton.grid(row=4, column=1,padx=10,
                                                  pady=10, sticky="nsw")

        self.home_frame_entry = CTkOptionMenu(
            self.home_frame, values=["Город"] + [i[0] for i in rowsh if self.poisk in i or self.poisk == '']
            , width=200, height=50)
        self.home_frame_entry.grid(row=4, column=2,padx=10,
                                           pady=10, sticky="nsw")
        self.home_frame_entry_name = CTkEntry(
            self.home_frame, placeholder_text="Название места", width=200, height=50)
        self.home_frame_entry_name.grid(row=4, column=3,
                                            padx=10, pady=10, sticky="nsw")
        self.home_frame_entry_vid = CTkOptionMenu(
            self.home_frame, values=["Вид",
                "исторический памятник", "здание", "природный объект", "парк", "музей",
                "скульптура", "монастырь", "храм"], width=200, height=50)
        self.home_frame_entry_vid.grid(row=4, column=4,padx=10,
                                               pady=10, sticky="nsw")

        self.home_frame_entry2_buton_1 = CTkButton(self.home_frame, text="Поиск", command=self.poisk_all)
        self.home_frame_entry2_buton_1.grid(row=4, column=5,padx=10,
                                                  pady=10, sticky="nsw")


        # создаем 3 фрейм
        self.second_frame = CTkFrame(self, corner_radius=0,
            fg_color="transparent")
        # Настройка
        self.navigation_frame2_label = CTkLabel(
            self.second_frame,
            text="Login: "+LOGIN,
            font=CTkFont(size=30, weight="bold"))
        self.navigation_frame2_label.grid(padx=200, pady=100)
        # создаем 2 фрейм
        self.third_frame = CTkFrame(self, corner_radius=0,
            fg_color="transparent")
        # создаём 4 фрейм
        self.pozitive_frame = CTkFrame(self, corner_radius=0,
                                                   fg_color="transparent")
        self.pozitive_frame_Lable = CTkLabel(self.pozitive_frame,
                                  text='В этих местах я уже был',
                                  font=CTkFont(size=30, weight="bold"))
        self.pozitive_frame_Lable.grid()
        self.pozitive_frame_None = CTkLabel(self.pozitive_frame,
                                  text='', )
        self.pozitive_frame_None.grid(row=1, column=0)
        self.pozitive_frame_None = CTkLabel(self.pozitive_frame,
                                            text='', )
        self.pozitive_frame_None.grid(row=2, column=0)
        self.pozitive_frame_None = CTkLabel(self.pozitive_frame,
                                            text='', )
        self.pozitive_frame_None.grid(row=3, column=0)


        # создаём 5 фрейм
        self.negative_frame = CTkFrame(self, corner_radius=0,
                                                fg_color="transparent")
        self.negative_frame_Lable = CTkLabel(self.negative_frame,
                                  text='В этих местах я не хочу быть',
                                  font=CTkFont(size=30, weight="bold"))
        self.negative_frame_Lable.grid()
        self.pozitive_frame_None = CTkLabel(self.negative_frame,
                                            text='', )
        self.pozitive_frame_None.grid(row=1, column=0)
        self.pozitive_frame_None = CTkLabel(self.negative_frame,
                                            text='', )
        self.pozitive_frame_None.grid(row=2, column=0)
        self.pozitive_frame_None = CTkLabel(self.negative_frame,
                                            text='', )
        self.pozitive_frame_None.grid(row=3, column=0)
        self.pozitive_frame.grid_columnconfigure(0, weight=1)
        self.negative_frame.grid_columnconfigure(0, weight=1)
        global tk_textbox,tk_textbox_pozitive,tk_textbox_negative
        self.tk_textbox_pozitive = CTkScrollableFrame(self.pozitive_frame,
                                        height=screen_height - 250)
        self.tk_textbox_pozitive.grid(sticky="nsew")
        self.tk_textbox_pozitive.grid_columnconfigure((0,1,2,3,4), weight=1)

        self.tk_textbox_negative = CTkScrollableFrame(self.negative_frame,
                                        height=screen_height - 250)
        self.tk_textbox_negative.grid(sticky="nsew")
        self.tk_textbox_negative.grid_columnconfigure((0,1,2,3,4), weight=1)

        self.tk_textbox = CTkScrollableFrame(self.home_frame,
                                height=screen_height-250)
        self.tk_textbox.grid(row=5, columnspan=10, sticky="nsew")
        self.tk_textbox.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.home_Lable_Site = CTkLabel(self.tk_textbox,
                                       text='Город',
                                       font=CTkFont(size=30, weight="bold"))
        self.home_Lable_Site.grid(row=0, column=0)
        self.home_Lable_Name = CTkLabel(self.tk_textbox,
                                        text='Название',
                                        font=CTkFont(size=30, weight="bold"))
        self.home_Lable_Name.grid(row=0, column=1)
        self.home_Lable_Opis = CTkLabel(self.tk_textbox,
                                        text='Описание',
                                        font=CTkFont(size=30, weight="bold"))
        self.home_Lable_Opis.grid(row=0, column=2)
        self.home_Lable_Vid = CTkLabel(self.tk_textbox,
                                        text='Вид',
                                        font=CTkFont(size=30, weight="bold"))
        self.home_Lable_Vid.grid(row=0, column=3)
        self.home_Lable_Pol = CTkLabel(self.tk_textbox,
                                        text='Уже был',
                                        font=CTkFont(size=30, weight="bold"))
        self.home_Lable_Pol.grid(row=0, column=4)
        self.home_Lable_Neg = CTkLabel(self.tk_textbox,
                                        text='Не хочу быть',
                                        font=CTkFont(size=30, weight="bold"))
        self.home_Lable_Neg.grid(row=0, column=5)


        self.home_masive_install()
        # Настройка
        self.navigation_frame_label = CTkLabel(self.third_frame,
        text="В пишите данные для добавления новых мест",
        font=CTkFont(size=30, weight="bold"))
        self.navigation_frame_label.grid(padx=200, pady=100)
        j = 1
        self.home_frame_frame_2_entry2 = CTkEntry(
            self.third_frame, placeholder_text="Назвоние города", width=1000, height=50)
        self.home_frame_frame_2_entry2.grid(row=j, column=0,
                                                padx=200, pady=10, sticky="nsw")
        j+=1
        global poisk
        self.home_frame_frame_2_entry2_buton = CTkButton(self.third_frame, text="Поиск города", command=self.pois)
        self.home_frame_frame_2_entry2_buton.grid(row=j, column=0,
                                                padx=200, pady=10, sticky="nsw")
        j+=1
        self.home_frame_frame_2_entry = CTkOptionMenu(
            self.third_frame, values=["Город"]+[i[0] for i in rowsh if self.poisk in i or self.poisk=='']
            , width=1000, height=50)
        self.home_frame_frame_2_entry.grid(row=j, column=0,
                                    padx=200, pady=10, sticky="nsw")
        j+=1

        self.home_frame_frame_2_entry_name = CTkEntry(
            self.third_frame, placeholder_text="Название", width=1000, height=50)
        self.home_frame_frame_2_entry_name.grid(row=j, column=0,
                                    padx=200, pady=10, sticky="nsw")
        j += 1

        self.home_frame_frame_2_entry_opis = CTkEntry(
            self.third_frame, placeholder_text="Описание", width=1000, height=50)
        self.home_frame_frame_2_entry_opis.grid(row=j, column=0,
                                    padx=200, pady=10, sticky="nsw")
        j += 1

        self.home_frame_frame_2_entry_vid = CTkOptionMenu(
            self.third_frame, values=[
                "исторический памятник", "здание", "природный объект", "парк", "музей",
                "скульптура", "монастырь", "храм"],width=1000, height=50)
        self.home_frame_frame_2_entry_vid.grid(row=j, column=0,
                                    padx=200, pady=10, sticky="nsw")
        j += 1

        self.bitin_2frame = CTkButton(self.third_frame
            , text='Отправить на проверку', height=50, command=self.sql_new)
        self.bitin_2frame.grid(row=j, column=0, padx=200, pady=10)
        j += 1

        self.Error = CTkLabel(self.third_frame
            , text='', height=50)
        self.Error.grid(row=j, column=0)
        # Главный фрейм
        self.select_frame_by_name(FRAMGL_NAME)
    def sql_new(self):
        citi = self.home_frame_frame_2_entry.get()
        name = self.home_frame_frame_2_entry_name.get()
        opis = self.home_frame_frame_2_entry_opis.get()
        vid = self.home_frame_frame_2_entry_vid.get()
        if citi != '' and name != '' and opis != '' and citi != 'Город':
            self.Error.configure(text="Внесено в базу данных")
            opisenie_cursor.execute('''CREATE TABLE IF NOT EXISTS cities
                                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name TEXT NOT NULL,
                                 description TEXT NOT NULL,
                                 location TEXT NOT NULL);''')
            add_city_opis(len_txt(citi,24), len_txt(name,26), len_txt(opis,62), vid)
            opisenie.commit()
        else:
            self.Error.configure(text="Не всё заполнено")
    def pois(self):
        self.poisk = self.home_frame_frame_2_entry2.get()
        if self.poisk != "":
            self.poisk = self.poisk[0].upper() + self.poisk[1:].lower()
        self.home_frame_frame_2_entry.configure(values = ["Город"] + [i[0] for i in rowsh if (self.poisk in i[0]) or self.poisk == ''])
    def home_masive_install(self):
        global LOGIN, f
        p = open('file(sgl)/Логин', 'r', encoding="UTF-8")
        LOGIN = p.read()
        opisenie_cursor.execute('SELECT name,description,location,vid FROM cities')
        rows = opisenie_cursor.fetchall()
        f = 0
        for _ in rows:
            f += 1
        self.home_masive = []
        i = 0
        self.radio_var_poz = tkinter.IntVar(value=0)
        self.radio_var_neg = tkinter.IntVar(value=0)
        for row in rows:
            self.mas = [1,2,3,4,5,6]
            self.home_masive.append(self.mas)
            if str(i + 1) not in read_all(LOGIN):
                self.home_masive[i][0] = CTkLabel(self.tk_textbox, text=row[0])
                self.home_masive[i][1] = CTkLabel(self.tk_textbox, text=row[1])
                self.home_masive[i][2] = CTkLabel(self.tk_textbox, text=row[2])
                self.home_masive[i][3] = CTkLabel(self.tk_textbox, text=row[3])
                self.home_masive[i][4] = CTkRadioButton(self.tk_textbox,text='',width=0,
                                                        command=self.biton_pozitive, variable=self.radio_var_poz, value=i+1)
                self.home_masive[i][5] = CTkRadioButton(self.tk_textbox,text='',width=0,
                                                        command=self.biton_negetive, variable=self.radio_var_neg, value=i+1)
            elif str(i + 1) in read_pozitive(LOGIN):
                self.home_masive[i][0] = CTkLabel(self.tk_textbox_pozitive, text=row[0])
                self.home_masive[i][1] = CTkLabel(self.tk_textbox_pozitive, text=row[1])
                self.home_masive[i][2] = CTkLabel(self.tk_textbox_pozitive, text=row[2])
                self.home_masive[i][3] = CTkLabel(self.tk_textbox_pozitive, text=row[3])
                self.home_masive[i][4] = CTkRadioButton(self.tk_textbox_pozitive, text='Вернуть',width=0,
                                                        command=self.recers_pozitive, variable=self.radio_var_poz, value=i+1)
                self.home_masive[i][5] = CTkLabel(self.tk_textbox_pozitive, text='')
            else:
                self.home_masive[i][0] = CTkLabel(self.tk_textbox_negative, text=row[0])
                self.home_masive[i][1] = CTkLabel(self.tk_textbox_negative, text=row[1])
                self.home_masive[i][2] = CTkLabel(self.tk_textbox_negative, text=row[2])
                self.home_masive[i][3] = CTkLabel(self.tk_textbox_negative, text=row[3])
                self.home_masive[i][4] = CTkRadioButton(self.tk_textbox_negative, text='Вернуть',width=0,
                                                        command=self.recers_negative, variable=self.radio_var_neg, value=i+1)
                self.home_masive[i][5] = CTkLabel(self.tk_textbox_negative, text='')
            i+=1
        self.home_masive_grid(f)
    def recers_pozitive(self):
        global LOGIN
        self.home_masive_delite(f)
        self.pozitive = read_pozitive(LOGIN)
        opisenie_cursor.execute('SELECT name,description,location FROM cities')
        self.pozitive.remove(str(self.radio_var_poz.get()))
        self.pozitive = json.dumps(self.pozitive)
        c.execute(f'UPDATE users SET array1 = ? WHERE login = ?',
        (self.pozitive, LOGIN))
        conn.commit()
        self.home_masive_install()
        self.home_masive_grid(f)
        self.pozitive = read_pozitive(LOGIN)
    def recers_negative(self):
        global LOGIN
        self.home_masive_delite(f)
        self.negative = read_negativ(LOGIN)
        opisenie_cursor.execute('SELECT name,description,location FROM cities')
        self.negative.remove(str(self.radio_var_neg.get()))
        self.negative = json.dumps(self.negative)
        c.execute(f'UPDATE users SET array2 = ? WHERE login = ?',
        (self.negative, LOGIN))
        conn.commit()
        self.home_masive_install()
        self.home_masive_grid(f)
        self.negative = read_negativ(LOGIN)
    def biton_pozitive(self):
        self.home_masive_delite(f)
        self.pozitive = read_pozitive(LOGIN)
        opisenie_cursor.execute('SELECT name,description,location FROM cities')
        self.pozitive += str(self.radio_var_poz.get())
        self.pozitive = json.dumps(self.pozitive)
        c.execute(f'UPDATE users SET array1 = ? WHERE login = ?'
        , (self.pozitive, LOGIN))
        conn.commit()
        self.home_masive_install()
        self.home_masive_grid(f)
        self.pozitive = read_pozitive(LOGIN)
    def biton_negetive(self):
        self.home_masive_delite(f)
        self.negative = read_negativ(LOGIN)
        opisenie_cursor.execute('SELECT name,description,location FROM cities')
        self.negative += str(self.radio_var_neg.get())
        self.negative = json.dumps(self.negative)
        c.execute(f'UPDATE users SET array2 = ? WHERE login = ?'
                  , (self.negative, LOGIN))
        conn.commit()
        self.home_masive_install()
        self.home_masive_grid(f)
        self.negative = read_negativ(LOGIN)
    def home_masive_grid(self, f):
        for i in range(f):
            if str(i+1) not in read_all(LOGIN):
                if self.proverka(self.home_masive[i][0].cget("text"),
                self.home_masive[i][1].cget("text"),
                self.home_masive[i][3].cget("text")):
                    self.home_masive[i][0].grid(row=i + 2, column=0)
                    self.home_masive[i][1].grid(row=i + 2, column=1)
                    self.home_masive[i][2].grid(row=i + 2, column=2)
                    self.home_masive[i][3].grid(row=i + 2, column=3)
                    self.home_masive[i][4].grid(row=i + 2, column=4)
                    self.home_masive[i][5].grid(row=i + 2, column=5)
            else:
                self.home_masive[i][0].grid(row=i + 2, column=0)
                self.home_masive[i][1].grid(row=i + 2, column=1)
                self.home_masive[i][2].grid(row=i + 2, column=2)
                self.home_masive[i][3].grid(row=i + 2, column=3)
                self.home_masive[i][4].grid(row=i + 2, column=4)
    def home_masive_delite(self, f):
        for i in range(f):
            self.home_masive[i][0].destroy()
            self.home_masive[i][1].destroy()
            self.home_masive[i][2].destroy()
            self.home_masive[i][3].destroy()
            self.home_masive[i][4].destroy()
            self.home_masive[i][5].destroy()
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
        add_user(LOGIN, password,['0'],['0'])
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
            p.close()
            return 0
        p.close()
        return self.avtor(password)
    def proverka(self, cite, name, vid):
        return ((self.cites_poisk == cite or self.cites_poisk == "") and
                (self.name_poisk in name) and
                (self.vid_poisk == vid or self.vid_poisk == ""))


if __name__ == "__main__":
    app = App()
    app.mainloop()
    conn.close()
    site.close()
    opisenie.close()
