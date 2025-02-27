import mysql.connector
from mysql.connector import Error

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.success_on_connecting = False

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            self.success_on_connecting = True

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def get_cursor(self):
        if self.connection and self.connection.is_connected():
            return self.connection.cursor(dictionary=True)
        else:
            raise Exception("Connection is not established. Call connect() first.")
        
    def commit(self):
        self.connection.commit()
