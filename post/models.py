import sqlite3

from sqlite3 import Error, IntegrityError, OperationalError
from manager import db_path
 

def create_new_post(content, username):
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = f'INSERT INTO posts (content, user_id) VALUES (\'{content}\', (SELECT id FROM users WHERE username = \'{username}\'));'
    crsr.execute(command)
    conn.commit()
    conn.close()


def get_all_posts():
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = 'select content, users.username from posts inner join users on  users.id = posts.user_id;'
    posts = crsr.execute(command)
    posts = posts.fetchall()
    posts = [{'content':content, 'username': username} for content, username in posts]
    conn.close()
    return posts
