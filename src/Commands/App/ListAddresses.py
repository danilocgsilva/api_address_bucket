from src.Builder import Builder
from src.Commands.CommandInterface import CommandInterface

class ListAddresses(CommandInterface):
    def __init__(self):
        builder = Builder()
        self.addressRepository = builder.getAddressRepository()
        
    def execute(self):
        addresses = self.addressRepository.all()
        for address in addresses:
            print("* " + address.address)
