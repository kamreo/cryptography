import sqlite3

def create_database():
    '''Module for connecting to sqlite database'''
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    #creating table
    c.execute("""CREATE TABLE IF NOT EXISTS users (
            login text,
            email text,
            password text,
            hash text
        )""")
    #exexuting command
    conn.commit()
    #closing connection
    conn.close()

def insert_user(login, email, hashed_password, salt):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?,?)", (login, email, hashed_password, salt))
    conn.commit()
    conn.close()

def get_user(login):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE login = ?", (login,))
    data = c.fetchall()
    conn.close()
    if data:
        return data[0]
    else: 
        return False