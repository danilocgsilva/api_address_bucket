from src.Models.Addess import Address
from Repositories.AddressRepository import AddressRepository
from src.Builder import Builder
import unittest

class AddressRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.builder = Builder().setTest()
        self.addressRepository = self.builder.getAddressRepository()
        
    def test_empty_database(self):
        self.resetDatabase()
        addresses = self.addressRepository.all()
        self.assertEqual(0, len(addresses))
        
    def test_addAndGet(self):
        self.resetDatabase()
        self.addressRepository.create("http://my.api.com")
        addresses = self.addressRepository.all()
        self.assertEqual(1, len(addresses))
        
    def test_searchByAddress(self):
        self.resetDatabase()
        self.addressRepository.create("http://my.api.com")
        address = self.addressRepository.searchByAddress("http://my.api.com")
        self.assertIsInstance(address, Address)
        
    def test_searchByAddressNotExisting(self):
        self.resetDatabase()
        self.addressRepository.create("http://my.api.com")
        address = self.addressRepository.searchByAddress("http://non_existent_api")
        self.assertTrue(address is None)
        
    def resetDatabase(self):
        connection = self.builder.getConnection()
        cursor = connection.get_cursor()
        
        query1 = "DELETE FROM addresses"
        cursor.execute(query1)
        
        query2 = "ALTER TABLE addresses AUTO_INCREMENT = 1"
        cursor.execute(query2)
        
if __name__ == '__main__':
    unittest.main()
