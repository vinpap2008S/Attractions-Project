import sqlite3

# Создаем подключение к базе данных или открываем существующую
site = sqlite3.connect('cities.db')

# Создаем таблицу, если она не существует
site.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL);''')

def add_city(name):
    # Добавляем новый город в базу данных
    site.execute("INSERT INTO cities (name) VALUES (?)", (name,))
    site.commit()
    print("Город успешно добавлен!")

def check_city(name):
    # Проверяем наличие города в базе данных
    cursor = site.execute("SELECT name FROM cities WHERE name=?", (name,))
    city = cursor.fetchone()
    if city:
        print(f"Город {name} найден в базе данных!")
    else:
        print(f"Город {name} не найден в базе данных!")

# Пример использования функций
# add_city("Москва")
# add_city("Санкт-Петербург")
# check_city("Москва")
# check_city("Екатеринбург")

# Закрываем соединение с базой данных

site.close()