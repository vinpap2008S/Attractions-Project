FRAMGL_NAME = "Главная"
FRAM1_NAME = "Добавление обьектов"
FRAM2_NAME = "Профиль"
FRAM3_NAME = "Уже был"
FRAM4_NAME = "Не хочу быть"
import sqlite3
g = 0
def add_city_opis(name, description, location, vid):
    # Добавляем новый город описание в базу данных
    opisenie_cursor.execute("INSERT INTO cities (name, description, location, vid)"
                            " VALUES (?, ?, ?, ?)", (name, description, location, vid))
if g:
    opisenie = sqlite3.connect('file(sgl)/opisenie.db')
    opisenie_cursor = opisenie.cursor()
    while True:
        citi = input('Город\n')
        name = input('Название\n')
        opis = input('Описание\n')
        vid = input('Вид\n')
        if vid == 'v':
            break
        opisenie_cursor.execute('''CREATE TABLE IF NOT EXISTS cities
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     description TEXT NOT NULL,
                     location TEXT NOT NULL);''')
        add_city_opis(citi, name, opis, vid)
        opisenie.commit()
