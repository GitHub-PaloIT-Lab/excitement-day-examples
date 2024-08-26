import sqlite3

class User:
    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get_user_by_username(username):
        user = None
        connection_string = "your_database.db"
        query = f"SELECT * FROM Users WHERE Username = '{username}'"  # Vulnerable to SQL injection

        connection = sqlite3.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            user = User(id=row[0], username=row[1], password=row[2])

        connection.close()
        return user
