from src.Commands.App.AddAddress import AddAddress
from src.Commands.App.ListAddresses import ListAddresses
from src.Commands.App.TestAddress import TestAddress
from src.Commands.Dev.CreateTestDatabase import CreateTestDatabase
from src.Commands.Dev.CreateDatabase import CreateDatabase
from src.Commands.Dev.MigrateTestDatabase import MigrateTestDatabase

commands = {
    "add address": AddAddress(),
    "list addresses": ListAddresses(),
    "test address": TestAddress(),
    "create test database": CreateTestDatabase(),
    "create database": CreateDatabase(),
    "migrate test database": MigrateTestDatabase(),
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

