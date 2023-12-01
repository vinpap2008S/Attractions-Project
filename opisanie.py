import sqlite3

# Создаем подключение к базе данных или открываем существующую
conn = sqlite3.connect('cities.db')

# Создаем таблицу, если она не существует
conn.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             description TEXT NOT NULL);''')

def add_city(name, description):
    # Добавляем новый город в базу данных
    conn.execute("INSERT INTO cities (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    print("Город успешно добавлен!")

def get_city_info(name):
    # Получаем информацию о городе по его названию
    cursor = conn.execute("SELECT description FROM cities WHERE name=?", (name,))
    city_info = cursor.fetchone()
    if city_info:
        print(f"Описание города {name}: {city_info[0]}")
    else:
        print("Город не найден!")

# Пример использования функций
add_city("Москва", "Столица России")
add_city("Санкт-Петербург", "Город на Неве")
get_city_info("Москва")
get_city_info("Санкт-Петербург")

# Закрываем соединение с базой данных
conn.close()