from pet_simulator import Pet

my_adorable_pet = Pet()

pet_name = input("Enter pet name: ")
animal_type = input("Enter pet type: ")
pet_age = input("Enter pet age: ")

my_adorable_pet.set_name(pet_name)
my_adorable_pet.set_animal_type(animal_type)
my_adorable_pet.set_age(pet_age)

print("Here is the information of your pet: ")
print(f"Name: {my_adorable_pet.get_name()}")
print(f"Animal Type: {my_adorable_pet.get_animal_type()}")
print(f"Age: {my_adorable_pet.get_age()}")
