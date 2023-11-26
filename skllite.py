import sqlite3
def add_user(login, password, array1, array2):
    c.execute('''
        INSERT INTO users (login, password, array1, array2)
        VALUES (?, ?, ?, ?)
    ''', (login, password, array1, array2))
    conn.commit()
    print("Пользователь успешно добавлен!")
def get_users():
    c.execute('SELECT * FROM users')
    rows = c.fetchall()
    for row in rows:
        print(row)
def delete_user(login):
    c.execute('DELETE FROM users WHERE login=?', (login,))
    conn.commit()
    print("Пользователь успешно удален!")
def read_column(column_name):
    c.execute(f'SELECT {column_name} FROM users')
    rows = c.fetchall()
    for row in rows:
        print(row[0])
