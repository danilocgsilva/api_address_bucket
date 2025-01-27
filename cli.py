from src.Commands.AddAddress import AddAddress
from src.Commands.ListAddresses import ListAddresses
from src.Commands.TestAddress import TestAddress

commands = {
    "add address": AddAddress(),
    "list addresses": ListAddresses(),
    "test address": TestAddress(),
}

print("Here follows the options available:")
for k, v in commands.items():
    print("* " + k)

choosed = input("Choose one! ")

print(f"You choosed {choosed}")
if choosed in commands:
    commands[choosed].execute()
else:
    print("You choosed something that does not exists.")

