from src.Builder import Builder

class ListAddresses:
    def __init__(self):
        builder = Builder()
        self.addressRepository = builder.getAddressRepository()
        
    def execute(self):
        addresses = self.addressRepository.all()
        for address in addresses:
            print("* " + address.address)
