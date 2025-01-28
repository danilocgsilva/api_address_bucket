from src.Builder import Builder
import os

class MigrateTestDatabase:
    def __init__(self):
        self.builder = Builder().setTest()
        self.connection = None
        
    def migrate_addresses(self):
        if not self.connection:
            self.connection = self.builder.getConnection()
        database_migration_script_file = self.getScriptPath("create_table.sql")
        migration_file = open(database_migration_script_file)
        file_content = migration_file.read()
        cursor = self.connection.get_cursor()
        cursor.execute(file_content)
        
    def migrate_tests_results(self):
        if not self.connection:
            self.connection = self.builder.getConnection()
        
    def execute(self):
        self.migrate_addresses()
        print("Migration successfully done!")
        
    def getScriptPath(self, script_name):
        current_module_path = os.path.dirname(os.path.abspath(__file__))
        database_migration_script_file = os.path.join(current_module_path, "..", "..", "..", "database", script_name)
        return database_migration_script_file
        
        