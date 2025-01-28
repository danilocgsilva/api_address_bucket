from src.Models.TestResult import TestResult

class TestsResultsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.table_name = "tests_results"

    def all(self) -> list:
        cursor = self.db_connection.get_cursor()
        query = f'SELECT success, address_id, date FROM {self.table_name}'
        cursor.execute(query)
        rows = cursor.fetchall()
        results_fetched = []
        for row in rows:
            results_fetched.append(TestResult(row["result"]))
        return results_fetched

    def get_by_id(self, result_id):
        cursor = self.db_connection.get_cursor()
        query = f'SELECT success, address_id, date FROM {self.table_name} WHERE id = %s'
        cursor.execute(query, (result_id,))
        raw_data = cursor.fetchone()
        if raw_data:
            return TestResult(raw_data["success"], raw_data["address_id"], raw_data["date"])
        return None

    def create(self, success, address_id, date):
        cursor = self.db_connection.get_cursor()
        query = f'INSERT INTO {self.table_name} (success, address_id, date) VALUES (%s, %s, %s)'
        cursor.execute(query, (success, address_id, date, ))
        self.db_connection.connection.commit()

    def delete(self, result_id):
        cursor = self.db_connection.get_cursor()
        query = f'DELETE FROM {self.table_name} WHERE id = %s'
        cursor.execute(query, (result_id, ))
        self.db_connection.connection.commit()

    def search_by_address_id(self, address_id):
        cursor = self.db_connection.get_cursor()
        query = f'SELECT success, address_id, date FROM {self.table_name} WHERE address_id = %s'
        cursor.execute(query, (address_id, ))
        raw_data = cursor.fetchone()
        if raw_data:
            return TestResult(raw_data["success"], raw_data["address_id"], raw_data["date"])
        else:
            return None