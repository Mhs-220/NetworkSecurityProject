import sqlite3

from sqlite3 import Error, OperationalError, IntegrityError

from manager     import db_path

def create_post():
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = """
    create table posts(
        id integer primary key autoincrement,
        content text not null,
        created_date text default (DATETIME('now')),
        user_id integer not null,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """
    try:
        crsr.execute(command)
        print('Posts Table Created.')
    except OperationalError as oe:
        print(oe)
    finally:
        conn.close()

def create_test_post():
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = "insert into posts(content, user_id) values (?,?);"
    values = ('TEST', 1)
    try:
        result = crsr.execute(command, values)
        conn.commit()
        print(f'Test post create with {result.lastrowid} id.')
    except OperationalError as oe:
        print(oe)
    except IntegrityError as ie:
        print(ie)
    finally:
        conn.close()

