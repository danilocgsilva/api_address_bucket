from src.AddressRepository import AddressRepository
from src.MySQLConnection import MySQLConnection
import os

class Builder:
    def getAddressRepository(self):
        myConnection = MySQLConnection(
            host=os.environ.get("DATABASE_HOST"),
            user=os.environ.get("DATABASE_USER"),
            password=os.environ.get("DATABASE_PASSWORD"),
            database=os.environ.get("DATABASE_NAME")
        )
        myConnection.connect()
        addressRepository = AddressRepository(myConnection)
        return addressRepository