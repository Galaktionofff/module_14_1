import sqlite3
import random

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")
for i in range(1, 9 + 1):
    cursor.execute(" INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'username{i}', f'{i}ex@mail.ru', i * 10, random.choice([500])))
cursor.execute(" UPDATE Users SET balance = balance + 500 WHERE id % 2 == 0")
for i in range(1, 9 + 1, 3):
    cursor.execute(" DELETE FROM Users WHERE id = ?", (i, ))
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
users = cursor.fetchall()
for user in users:
    username, email, age, balance = user
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')
# cursor.execute(" DELETE FROM Users")
connection.commit()
connection.close()
