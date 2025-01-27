from src.Commands.CommandInterface import CommandInterface
from src.Builder import Builder
import os

class CreateTestDatabase(CommandInterface):
    def __init__(self):
        self.connection = Builder().getConnection()
    
    def execute(self):
        database_name = os.environ.get("DATABASE_NAME_TEST")
        query = f"CREATE DATABASE {database_name}"
        cursor = self.connection.get_cursor()
        cursor.execute(query)
