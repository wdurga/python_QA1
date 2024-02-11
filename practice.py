#Q2. WAP to print single and double quotes. : Hello I am “John Doe”
#message print using single quote inside double quote
"""double_quote = ("Hello I'm John Doe.")
print(double_quote)
#message prit using doule quote inside single quote
single_quote = ('Hello, i am "john doe"')
print(single_quote)"""
#Q3. WAP that finds Simple Interest, formula = (p*t*r)/100.
"""print("Calculate using simple interest formula")
p = int(input("Enter principle amount : "))
t = float(input("Enter time period : "))
r = int(input("Enter interest rate : "))
si = (p*t*r)/100
print(si)"""
#Q4. WAP to print square of a number using user input.
"""number = int(input("Square of a number : "))
square = number ** 2
print(square)
#Q5. WAP to print cube of a number using user input.
number = int(input("Enter a number for cube : "))
cube = number ** 3
print(cube)
"""
#Q5. WAP to print Full Name from first and last name using user input.
"""first_name = input("Enter first name : ")
last_name = input("Enter last name : ")
full_name = first_name + " " + last_name
print(full_name)"""
#Q6. WAP to find Quotient and Remainder of two integer.
"""first_number = int(input("Enter a first number :"))
second_number = int(input("Enter a second number : "))
quotient = first_number//second_number
remainder = first_number%second_number
print("The quotient is {} and the remainder is {} ".format(quotient,remainder))"""
#Q7. WAP to swap two numbers.
"""a = int(input("enter value of A : "))
b = int(input("enter value of B : "))
temp = a
a = b
b = temp
print("After swapping : ")
print("value of A : ", a)
print("value of B : ", b)"""
#Q8. WAP to remove all white space from string.
"""string = ('Fuck you bitch')
print(string)
rstring = string.replace(" ", "")
print(rstring)"""
#Q9. WAP to convert string into int.
"""string_num = input("Enter a number :")
print("before type casting : " , type(string_num))
string_num = int(string_num)
print("After type casting : ", type(string_num))"""
#Q10. WAP to calculate split amount of bill. Formula = (total bill amount)/ number of people.
"""b = float(input("Enter total bill amount : "))
p = int(input("Enter number of people : "))
bill_split = b/p
print("The splitted bill among total number of people is :" , bill_split)
"""
#Q11. WAP to calculate time taken to reach office in minutes, Formula = (distance)/speed.
"""d = int(input("Distance to travel from office to home is "))
s = int(input("Speed travelling kmp hour is "))
timeinhour = d/s
timeinminute = timeinhour * 60
print("total time taken to travel from office to home is : " , timeinminute)"""
#Q12. WAP to check if Number is odd or even.
"""number = int(input("Enter a number to chek even or odd : "))
if (number % 2) == 0:
    print("the number {0} is even".format(number))
else:
    print("the number {0} is odd".format(number))"""

#Q13. WAP to check whether a character is a vowel or consonant.
"""ch = input("Enter a alphabet to determine vowel or consonsnt : ")
if ch in ('a','e','i','o','u','A','E','I','O','U'):
    print(ch, "is a vowel.")
else:
    print(ch,"is a consonant")"""
# Q14. WAP to check whether a given number is positive, negative or zero.
"""num = int(input("Enter a number to test positive, negative or zero : "))
if num > 0:
    print("It is a positive number.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")"""
#Q4. WAP to print square of a number using user input.
"""num = int(input("Enter a number to be squared : "))
square = num ** 2
print("The square of ", num , "is" ,square)"""
#Q1. WAP to print your name 100 times.
"""name = "Anshu ji"
print("Print your name 100 times....")
print((name + "\n") * 100)"""
"""name = "aaa"
for _ in range(20):
    print(name)"""
#using for loop
"""name = "ggg"
for _ in range(5):
    print(name)"""
#using multiply
"""name = "fuck"
print((name + "\n") * 12)"""
#Q2. WAP to calculate the sum of natural numbers.
"""num = int(input("Enter a natural number to be added: "))
if num < 0:
     print("Please enter positive number")
else:
    sum = 0
    while num>0:
        sum +=num
        num -= 1
        print(sum)"""
#mileyko for total sum at once.
"""num = int(input("Enter a number for sum of natural number : "))
if num < 0:
    print("please enter positive num")
else:
    sum = 0
    while num>0:
        sum +=num
        num -= 1
    print("The sum of all natural number:", sum)"""
#Q3. WAP to generate multiplication tables of 5.
"""num = int(input("Enter a number for multiplication table :"))
for i in range(5,13):
    print(num, '*', i, '=', num*i)
"""
"""num = int(input("Enter number multiplication : "))
for i in range(3,21):
    print(num, '*',i, '=', num*i)"""
#Q4. WAP to generate multiplication tables of 1-9.
"""mul = int(input("Enter number : "))
for i in range(1, mul+1):
    print("\n")
    for j in range(4,16):
        print(i,'*',j,'=',i*j)"""

"""mul = int(input("Enter number multiplication : "))
for i in range(1,mul+1):
    for j in range(2,12):
     print(i,'*', j, '=',i*j)"""
#Q6. WAP to print 1 to 100 but not 41.
"""for i in range(1,101):
    if i != 41:
        print(i)"""
#Q5. WAP to create a simple calculator that performs addition, subtraction, multiplication and division.
"""print("Mini Calculator")

num1 = float(input("Enter firat number here : "))
num2 = float(input("Enter second number here : "))

print("Press 1 for addition \n Press 2 for Substraction \n Press 3 for Multiplication \n press 4 for division \n Press 5 for Exit")
choice = int(input("Enter your choice number from 1-4: "))

if choice == 1:
    print("The addition of given two numbers is: ", num1 + num2)
elif choice == 2:
    print("The substraction of given two numbers is :", num1 - num2)
elif choice == 3:
    print("The multiplication of given two numbers is :", num1 * num2)
elif choice == 4:
    print("The division of given two numbers is : ", num1/num2)
elif choice == 5:
    print("Exit")
else:
    print("Input is not valid.")"""
#use of nested loop: star in rows pattern.
"""rows = int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(0,i):
        print("*",end=" ")
    print("")"""


def add_numbers(num1, num2):
    sum = num1 + num2
    return sum


def sub_numbers(num1, num2):
    substract = num1 - num2

    return substract


def multi_ply(num1, num2):
    multiply = num1 * num2
    return multiply


def total_result():
    first = float(input("Enter number: "))
    second = float(input("Enter number: "))

    return first, second


while True:
    print('''
      Enter the choice:
      1: Add
      2:Substract
      3: Multiply
      4: Exit
       ''')
    option = int(input("Enter the option: "))

    if option == 1:
        numbers = total_result()
        print("Total is: ", add_numbers(*numbers))
    elif option == 2:
        numbers = total_result()
        print("Total is: ", sub_numbers(*numbers))
    elif option == 3:
        multiply_result = total_result()
        print("Total is: ", multi_ply(*multiply_result))
    elif option == 4:
        exit()

    break

