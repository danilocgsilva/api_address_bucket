from src.Builder import Builder
import os

class MigrateTestDatabase:
    def __init__(self):
        self.connection = Builder().setTest().getConnection()
        
    def execute(self):
        current_module_path = os.path.dirname(os.path.abspath(__file__))
        database_migration_script_file = os.path.join(current_module_path, "..", "..", "..", "create_table.sql")
        migration_file = open(database_migration_script_file)
        file_content = migration_file.read()
        cursor = self.connection.get_cursor()
        cursor.execute(file_content)
        print("Migration successfully done!")
        
    