from src.Builder import Builder

builder = Builder()

addressRepository = builder.getAddressRepository()

address_to_be_added = input("Which is the address you want to register? ")
print(f'You want to add {address_to_be_added} to the database.')
addressRepository.create(address_to_be_added)
print(f'{address_to_be_added} successfully added to the database.')