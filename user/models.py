import sqlite3

from sqlite3 import Error
from manager import db_path

def valid_login(username, password):
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    # Hash password
    # check_for_sql_injection(username)
    # check_for_sql_injection(password)
    command = 'SELECT * FROM USERS WHERE USERNAME="{}" AND PASSWORD="{}"'.format(username, password)
    crsr.execute(command)
    conn.close()
    
    print('user logined')
    return False

def username_or_email_taken(username, email):
    # check_for_sql_injection(username)
    # check_for_sql_injection(email)
    print('checked email and username')
    return False

def create_new_user(form):
    return None

def get_user_profile(username):
    return None