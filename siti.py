import sqlite3
def add_city(name):# Добавляем новый город в базу данных
    site.execute("INSERT INTO cities (name) VALUES (?)", (name,))
    site.commit()

def check_city(name):# Проверяем наличие города в базе данных
    cursor = site.execute("SELECT name FROM cities WHERE name=?", (name,))
    city = cursor.fetchone()
    if city:
        return 1
    else:
        return 0
print(check_city("Москва"))
check_city("Екатеринбург")

# Закрываем соединение с базой данных

site.close()