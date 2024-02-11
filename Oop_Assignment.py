# 34. Write a python program to create a class Laptop with properties
# [id, name, RAM] and create 3 objects of it and print all details.

"""class Laptop:
    def __init__(self, id, name, ram):
        self.id = id
        self.name = name
        self.ram = ram

# Creating three objects of the Laptop class
l1 = Laptop(id=11, name="Dell", ram="4GB")
l2 = Laptop(id=24, name="Lenovo", ram="16GB")
l3 = Laptop(id=33, name="Acer", ram="8GB")

# Printing details of each laptop
print("Laptop 1 Details:")
print("ID:", l1.id)
print("Name:", l1.name)
print("RAM:", l1.ram)
print()

print("Laptop 2 Details:")
print("ID:", l2.id)
print("Name:", l2.name)
print("RAM:", l2.ram)
print()

print("Laptop 3 Details:")
print("ID:", l3.id)
print("Name:", l3.name)
print("RAM:", l3.ram)"""


# 35. Write a python program to create a class House with properties
# [id, name, prize]. Create a constructor of it and create
# 3 objects of it. Add them to the list and print all details.

"""class House:
    def __init__(self,id, name,price):
        self.id = id
        self.name = name
        self.price = price

h1 = House(1,'White House',50000)
h2 = House(2,'Black House', 60000)
h3 = House(3, 'Ghost House', 900000)

h_list = [h1,h2,h3]

for houses in h_list:
    print(f"ID: {houses.id}, name: {houses.name}, price: {houses.price}")"""

# 36. Write a python program to create an enum class
# for gender [male, female, others] and print all values.
"""from enum import Enum

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHERS = 'Others'

# Printing all values in the Gender Enum
for all_gender in Gender:
    print(all_gender.value)"""

"""from enum import Enum

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHERS = 3

for all_genders in (Gender):
    print(all_genders.value,"-", all_genders)"""

# 37.  Write a python program to create a class Animal with properties
# [id, name, color]. Create another class called Cat and
# extends it from Animal. Add new properties sound in String.
# Create an object of a Cat and print all details.

class Animal:
    def __init__(self,id,name,color):
        self.id = id
        self.name = name
        self.color = color

class Cat(Animal):
    def __init__(self,id, name, color,sound):
        super().__init__(id,name,color)
        self.sound = sound

c1 = Cat(11,'Biralo','Red','Meow')

print("Cat Details:")
print("ID:", c1.id)
print("Name:", c1.name)
print("Color:", c1.color)
print("Sound:", c1.sound)