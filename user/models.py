import os
import hashlib
import binascii
import sqlite3

from sqlite3 import Error, IntegrityError, OperationalError
from manager import db_path
 

def valid_login(username, password):
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    # Hash password
    # check_for_sql_injection(username)
    # check_for_sql_injection(password)
    command = 'SELECT password FROM USERS WHERE USERNAME=\'{}\''.format(username)
    user = crsr.execute(command)
    stored_password = user.fetchall()[0][0]
    is_verify = verify_password(stored_password, password)
    conn.close()
    if is_verify:
        return True
    return False


def username_or_email_taken(username, email):
    # check_for_sql_injection(username)
    # check_for_sql_injection(email)
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = 'SELECT password FROM USERS WHERE USERNAME=\'{}\' OR EMAIL=\'{}\''.format(username, email)
    user = crsr.execute(command)
    user = user.fetchall()
    conn.close()
    if len(user)>0:
        return True
    return False


def create_new_user(form):
    username = form['username']
    email = form['email']
    password = hash_password(form['password'])
    firstname = form['firstname']
    lastname = form['lastname']
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = 'insert into users (username, password, email, firstname, lastname) values (?,?,?,?,?);'
    values = (username, password, email, firstname, lastname)
    try:
        result = crsr.execute(command, values)
        conn.commit()
        print(f'Test user create with {result.lastrowid} id.')
    except IntegrityError as ie:
        print(ie)
    finally:
        conn.close()


def get_user_profile(username):
    conn = sqlite3.connect(db_path)
    crsr = conn.cursor()
    command = f'select * from users where username=\'{username}\';'
    try:
        result = crsr.execute(command)
        user_info = result.fetchall()[0]
        user_info = (info for index, info in enumerate(user_info) if index not in (0, 2) )
        username, email, firstname, lastname = user_info
        user_dict = {
            'username': username,
            'email': email,
            'firstname': firstname,
            'lastname': lastname
        }
    except OperationalError as oe:
        print(oe)
    except IntegrityError as ie:
        print(ie)
    finally:
        conn.close()

    return user_dict

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password