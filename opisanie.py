import sqlite3

# Создаем подключение к базе данных или открываем существующую
conn = sqlite3.connect('cities.db')

# Создаем таблицу, если она не существует
conn.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             description TEXT NOT NULL,
             location TEXT NOT NULL);''')

def add_city(name, description, location=""):
    # Добавляем новый город описание в базу данных
    conn.execute("INSERT INTO cities (name, description, location) VALUES (?, ?, ?)", (name, description, location))
    conn.commit()
    print("Город успешно добавлен!")

# Пример использования функций
# add_city("Москва", "Столица России", "Центральная Россия")
# add_city("Санкт-Петербург", "Город на Неве", "Северо-Западная Россия")
# check_city("Москва")
# check_city("Екатеринбург")

# Закрываем соединение с базой данных
conn.close()