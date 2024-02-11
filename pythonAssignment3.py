#Q1. WAP to print your name 100 times.
#using multiply operator
"""name = "Anshika Bhattarai"
print("Printing name 100 times...")
print((name + "\n") * 100)
"""
#using FOR loop
"""name = "ME"
for _ in range(100):
    print(name)"""

#Q2. WAP to calculate the sum of natural numbers.
"""n = int(input("Enter the number upto which you want to add: "))
sum = 0
i = 1
while (i<=n):
    sum = sum +i
    i=i+1
print("Sum of given natural number = ", sum)"""
#next way to find sum of natural number
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
#using FOR LOOP
"""n = int(input("Enter the number for multiplication table : "))
for i in range(1,11) :
    print(n, "*",i, "=", n*i)"""
#using WHILE LOOP
"""n = 8
i = 1
while i<=10:
    print(n,'*',i,'=',n*i)
    #i +=1 and i = i + 1 is same, it gives same result.
    i = i + 1"""

#Q4. WAP to generate multiplication tables of 1-9.
"""for x in range(1,10):
    print("Multiplication Table of %d is..." %x)
    for y in range(1,11):
        print(x, "*", y, "=", x*y)"""
#other ways to find multiplication tables of 1-9.
"""mul = int(input("Enter number multiplication : "))
for i in range(1,mul+1):
    for j in range(2,12):
     print(i,'*', j, '=',i*j)"""


#Q5. WAP to create a simple calculator that performs addition, subtraction, multiplication and division.
"""print(".......Mini Calculator.......")

num1 = float(input("Enter first number here: "))
num2 = float(input("Enter second number here: "))

print("Press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division \npress 5 for exit")
choice = int(input("Enter your choice from 1-4: "))

if choice == 1:
    print ("The addition of given two numbers is", num1 + num2)
elif choice == 2:
    print ("The substraction of given two numbers is", num1 - num2)
elif choice == 3:
    print ("The multiplication of given two numbers is", num1 * num2)
elif choice == 4:
    print ("The division of given two numbers is", num1 / num2)
elif choice == 5:
    print("Exit")
else:
    print("Input is not valid.")"""
#Q6. WAP to print 1 to 100 but not 41.
"""for i in range(1,101):
    if i !=41:
        print(i)"""
#Q7.use of nested loop: star in rows pattern.
"""rows = int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(0,i):
        print("*",end=" ")
    print("")"""
# Q8. WAP to check wheather the string is palindrome or not.
#METHOD 1:
"""original = input("Enter a string to check palindrome or not :")
reverse = original[::-1]
if original == reverse:
    print("String is pallindrome")
else:
    print("String is not pallindrome")"""
#rint("Reverse one", reverse)

#METHOD 2: no OUTPUT
"""original = input("Enter a string :")
reverse = ' '
for i in range(len(original)-1,-1,-1):
    reverse = reverse + original[i]
    if original == reverse:
        print("is pallindrome...")
    else:
        print("not pallindrome...")
    #print("Reverse one", reverse)"""
#METHOD 3: Best lagyo
"""original = input("Enter a string :")
reverse = original[-1::-1] #start value, End value, Step Value
if(original == reverse):
    print("Pallindrome ho")
else:
    print("Haina")"""
#Q9. Python program to print all prime numbers in an interval
"""lower = int(input("Enter lower limit here : "))
upper = int(input("Enter upper limit here : "))
for num in range (lower, upper + 1):
    if num>1:
        for i in range (2,num):
            if num % i == 0:
             break
        else:
            print(num)"""

