#Q2. WAP to print single and double quotes. : Hello I am “John Doe”
#message using double quote inside single quote
single_quote = ('Hello I am "John Doe"')
print(single_quote)

#message using single quote inside double quote
double_quote = ("hello I'm John Doe")
print(double_quote)

#Q3. WAP that finds Simple Interest, formula = (p*t*r)/100.
print("Program to calculate simple interest")
p=int(input("Enter the Principal amount = "))
t=float(input("Enter the Time = "))
r=float(input("Enter the Rate of Interest = "))
si=(p*t*r)/100
print("The calculated Simple Interest = ", si)

#Q4. WAP to print square of a number using user input.
number = int(input("Enter a Number :"))
square = number ** 2
print("Square of the number", number,"is:",square)


#Q5. WAP to print Full Name from first and last name using user input.
firstName = input("Enter your First Name : ")
lastName = input("Enter your last Name : ")
fullName = firstName + " " + lastName
print("My full name is : ", fullName)


#Q6. WAP to find Quotient and Remainder of two integer.
firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))
quotient = firstNum//secondNum
remainder = firstNum%secondNum
print("The quotient is {} and the remainder is {}".format(quotient,remainder))


#Q7. WAP to swap two numbers.
a = int(input("Enter the value for A: "))
b = int(input("Enter the value for B: "))
temp = a
a = b
b = temp
print("After Swapping: ")
print("Value of A:", a)
print("Value of B:", b)


#Q8. WAP to remove all white space from string.
string = "Hey Beautiful People"
print(string)
#using Replace
rstring = string.replace(" ", "")
print(rstring)


#Q9. WAP to convert string into int.
string_number = input("Enter a number: ")
print("Before type casting :", type(string_number))
string_number = int(string_number)
print("After type casting: ", type(string_number))


#Q10. WAP to calculate split amount of bill. Formula = (total bill amount)/ number of people.
total_bill_amount = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
split_amt = total_bill_amount / num_people
print("Splitted amount per person: ", split_amt)


#Q11. WAP to calculate time taken to reach office in minutes, Formula = (distance)/speed.
d= int(input("Enter total distance from home to office: "))
s = int(input("Enter speed kilometer per hour: "))
time_in_hour = d/s
time_in_minute = time_in_hour * 60
print("Time taken to reach office: ", time_in_minute)


#Q12. WAP to check if Number is odd or even.
number = int(input("Enter a number: "))
if (number % 2) == 0:
 print("{0} is even number".format(number))
else:
 print("{0} is odd number".format(number))


#Q13. WAP to check whether a character is a vowel or consonant.
ch = input("Enter the alphabet : ")
if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
 print(ch, "is a vowel")
else:
 print(ch,"is a consonant")


 #Q14. WAP to check whether a given number is positive, negative or zero.
num = int(input("Enter a number here : "))
if num > 0:
    print("It is a positive number.")
elif num == 0:
    print("It is zero.")
else:
    print("It is a negative number.")