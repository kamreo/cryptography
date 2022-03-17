import hashlib, uuid
import database

def insert_record_custom(login, email, password):
    password_data = hash(password)
    database.insert_user(login, email, password_data[0], password_data[1])

def insert_record_pbkdf2_hmac(login, email, password):
    password_data = hash_pbkdf2_hmac(password)
    database.insert_user(login, email, password_data[0], password_data[1])

def hash(plain_password, salt = 0):
    if salt == 0:
        salt = uuid.uuid4().hex
    return (hashlib.sha512((plain_password + salt).encode('utf-8')).hexdigest(), salt)

def check_password_custom_hash(login, password):
    user = database.get_user(login)
    if user:
        hashed_password = hash(password, user[3])
        return user[2] == hashed_password[0]
    return False

def hash_pbkdf2_hmac(plain_password, salt = 0):
    if salt == 0:
        salt = uuid.uuid4().hex
    return (hashlib.pbkdf2_hmac('sha512', plain_password.encode('utf-8'), salt.encode(),10000), salt)

def check_password_pbkdf2_hmac(login, password):
    user = database.get_user(login)
    if user:
        hashed_password = hash_pbkdf2_hmac(password, user[3])
        return user[2] == hashed_password[0]
    return False


'''Test functions for creating user and for user login'''
def custom_hash_insert_test():
    login = input("Podaj login: ")
    email = input("Podaj email: ")
    password1 = input("Podaj haslo: ")
    password2 = input("Powtorz haslo: ")

    if password1 == password2:
        insert_record_custom(login, email, password1)
        print('Pomyslnie dodano uzytkownika!')
    else:
        print('Hasla sie nie zgadzaja!')

def hash_pbkdf2_hmac_insert_test():
    login = input("Podaj login: ")
    email = input("Podaj email: ")
    password1 = input("Podaj haslo: ")
    password2 = input("Powtorz haslo: ")

    if password1 == password2:
        insert_record_pbkdf2_hmac(login, email, password1)
        print('Pomyslnie dodano uzytkownika!')
    else:
        print('Hasla sie nie zgadzaja!')

def custom_hash_login_test():
    login = input("Podaj login: ")
    password = input("Podaj haslo: ")

    if check_password_custom_hash(login, password):
        print('Pomyslnie zalogowano!')
    else:
        print('Dane logowania nieprawidlowe!')

def hash_pbkdf2_hmac_login_test():
    login = input("Podaj login: ")
    password = input("Podaj haslo: ")

    if check_password_pbkdf2_hmac(login, password):
        print('Pomyslnie zalogowano!')
    else:
        print('Dane logowania nieprawidlowe!')

database.create_database()
custom_hash_insert_test()
hash_pbkdf2_hmac_insert_test()
custom_hash_login_test()
hash_pbkdf2_hmac_login_test()


