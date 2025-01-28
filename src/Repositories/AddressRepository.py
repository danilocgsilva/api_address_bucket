from src.Models.Addess import Address

class AddressRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.table_name = "addresses"

    def all(self) -> list:
        cursor = self.db_connection.get_cursor()
        query = f'SELECT address FROM {self.table_name}'
        cursor.execute(query)
        rows = cursor.fetchall()
        address_fetched = []
        for row in rows:
            address_fetched.append(Address(row["address"]))
        return address_fetched

    def get_by_id(self, address_id):
        cursor = self.db_connection.get_cursor()
        query = f'SELECT address FROM {self.table_name} WHERE id = %s'
        cursor.execute(query, (address_id,))
        return cursor.fetchone()

    def create(self, address):
        cursor = self.db_connection.get_cursor()
        query = f'INSERT INTO {self.table_name} (address) VALUES (%s)'
        cursor.execute(query, (address, ))
        self.db_connection.connection.commit()

    def update(self, address_id, address):
        cursor = self.db_connection.get_cursor()
        query = f'UPDATE {self.table_name} SET address = %s WHERE id = %s'
        cursor.execute(query, (address, address_id))
        self.db_connection.connection.commit()

    def delete(self, address_id):
        cursor = self.db_connection.get_cursor()
        query = f'DELETE FROM {self.table_name} WHERE id = %s'
        cursor.execute(query, (address_id, ))
        self.db_connection.connection.commit()
        
    def searchByAddress(self, address):
        cursor = self.db_connection.get_cursor()
        query = f'SELECT address FROM {self.table_name} WHERE address = %s'
        cursor.execute(query, (address, ))
        raw_data = cursor.fetchone()
        if raw_data:
            return Address(raw_data["address"])
        else:
            return None