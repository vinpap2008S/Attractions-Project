import sqlite3
def add_city(name, description, location=""):
    # Добавляем новый город описание в базу данных
    opisenie.execute("INSERT INTO cities (name, description, location) VALUES (?, ?, ?)", (name, description, location))
    opisenie.commit()
    print("Город успешно добавлен!")

# Пример использования функций
# add_city("Москва", "Столица России", "Центральная Россия")
# add_city("Санкт-Петербург", "Город на Неве", "Северо-Западная Россия")
# check_city("Москва")
# check_city("Екатеринбург")

# Закрываем соединение с базой данных
opisenie.close()