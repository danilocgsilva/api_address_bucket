from src.Builder import Builder
from src.Commands.CommandInterface import CommandInterface
from src.AddressRepository import AddressRepository
from src.Builder import Builder

class TestAddress(CommandInterface):
    def __init__(self):
        self.address_repository = Builder().getAddressRepository()
    
    def execute(self):
        print("Choose the address to test. Type the option number:")
        choosedOptionsFromUser = self.getOptionFromUser()
        print(f"You choosed the option {choosedOptionsFromUser}")
            
    def getOptionFromUser(self):
        arrayKey = 0
        list_addresses = self.address_repository.all()
        for address in list_addresses:
            print(str(arrayKey) + ". ",end="")
            print(address.address)
            arrayKey += 1
        numberChoosed = input("Type here the option number to test: ")
        return list_addresses[int(numberChoosed)].address
        