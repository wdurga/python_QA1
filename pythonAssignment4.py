#Q1. WAP to print your own name using function.
"""def my_name():
    print('Anshika')
my_name()"""

"""class Name:
    def __init__(self,name):
        self.name = name
    def show_name_details(self):
        print('My own name is', self.name)

n1 = Name ('Anshika')
n1.show_name_details()"""

# Q2. WAP in python to print even numbers between intervals using function.
"""def Even_Numbers(start,end):
    for num in range (start,end+1):
        if num % 2 == 0:
            print(num)

Even_Numbers(6,20)
"""
#WAP in python to print odd and even number in a list.
"""list = [11,1,4,6,3,99,7,0]
for i in list:
    if(i % 2 == 0):
        print(i, "is even")
    else:
        print(i, "is odd")"""

# Q.3. Create a function called greet that takes a name as an argument and prints a greeting message.
# For example greet(“John”) should print “Hello, John”.
"""def greet(name):
    print('Hello, ' + name)

greet("John")"""

# Q.n.5. WAP in python that find the area of a circle using function . Formula: pi*r*r
import math
def area_of_circle(radius):
    area = math.pi * radius**2
    return area

#Q.7. WAP in python to calculate power of a certain number. For eg. 5^3=125.
"""def power_of_number(base, exponent):
    return base ** exponent
result = power_of_number(5, 3)
print("The power of given number 5^3 is ", result)"""

