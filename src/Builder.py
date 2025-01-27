from src.AddressRepository import AddressRepository
from src.MySQLConnection import MySQLConnection
import os

class Builder:
    def __init__(self):
        self.test = False
        
    def setTest(self):
        self.test = True
        return self
    
    def getAddressRepository(self):
        myConnection = self.getConnection()
        addressRepository = AddressRepository(myConnection)
        return addressRepository
    
    def getConnection(self):
        database_name = None
        if self.test:
            database_name = os.environ.get("DATABASE_NAME_TEST")
        else:
            database_name = os.environ.get("DATABASE_NAME")
        
        myConnection = MySQLConnection(
            host=os.environ.get("DATABASE_HOST"),
            user=os.environ.get("DATABASE_USER"),
            password=os.environ.get("DATABASE_PASSWORD"),
            database=database_name
        )
        myConnection.connect()
        return myConnection
        