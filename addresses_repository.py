class AddressRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.table_name = "addresses"

    def all(self):
        cursor = self.db_connection.get_cursor()
        query = f'SELECT * FROM {self.table_name}'
        cursor.execute(query)
        return cursor.fetchall()

    def get_by_id(self, address_id):
        cursor = self.db_connection.get_cursor()
        query = f'SELECT * FROM {self.table_name} WHERE id = %s'
        cursor.execute(query, (address_id,))
        return cursor.fetchone()

    def create(self, address):
        cursor = self.db_connection.get_cursor()
        query = f'INSERT INTO {self.table_name} (address) VALUES (%s)'
        cursor.execute(query, (address))
        self.db_connection.connection.commit()

    def update(self, address_id, address):
        cursor = self.db_connection.get_cursor()
        query = f'UPDATE {self.table_name} SET address = %s WHERE id = %s'
        cursor.execute(query, (address, address_id))
        self.db_connection.connection.commit()

    def delete(self, address_id):
        cursor = self.db_connection.get_cursor()
        query = f'DELETE FROM {self.table_name} WHERE id = %s'
        cursor.execute(query, (address_id,))
        self.db_connection.connection.commit()
