import sqlite3

from sqlite3 import Error, OperationalError, IntegrityError

from manager     import db_path
from user.models import hash_password

def create_user():
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = """
    create table users(
        id integer primary key autoincrement,
        username varchar(64) unique,
        password varchar(256),
        email varchar(64) unique,
        firstname varchar(64),
        lastname varchar(64)
    );
    """
    try:
        crsr.execute(command)
        print('Users Table Created.')
    except OperationalError as oe:
        print(oe)
    finally:
        conn.close()

def create_test_user():
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = "insert into users(username, password, email, firstname, lastname) values (?,?,?,?,?);"
    password = hash_password('123456')
    values = ('mhs', password, 'mhs@mhs.com', 'mhs', 'mhs')
    try:
        result = crsr.execute(command, values)
        conn.commit()
        print(f'Test user create with {result.lastrowid} id.')
    except OperationalError as oe:
        print(oe)
    except IntegrityError as ie:
        print(ie)
    finally:
        conn.close()

