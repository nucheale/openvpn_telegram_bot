import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        with self.connection:
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, bot_id INTEGER, status INTEGER CHECK(status IN (0, 1)), time TEXT)')
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS commands (id INTEGER PRIMARY KEY AUTOINCREMENT, command_name TEXT, command_description TEXT, count_calls INTEGER)')
            return

    def print_users_db(self):
        self.cursor.execute('SELECT * FROM users')
        users = self.cursor.fetchall()
        return users

    def user_exists(self, bot_user_id):
        result = self.cursor.execute(f"SELECT * FROM users WHERE bot_id = '{bot_user_id}'").fetchone()
        if result is None:
            return False
        else:
            return True

    def add_user(self, username, bot_user_id):
        with self.connection:
            self.cursor.execute(
                f"INSERT INTO users (name, bot_id) SELECT '{username}', '{bot_user_id}' WHERE NOT EXISTS (SELECT 1 FROM users WHERE bot_id = '{bot_user_id}')")
            self.cursor.execute(f"UPDATE users SET status = 1 WHERE bot_id = '{bot_user_id}'")
            return
