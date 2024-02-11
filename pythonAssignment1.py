# python single line comment
'''
Python multiple line comments. It also includes double quotation.
We can do multiple lines comments at a time.
'''
print("Hello All")

# python Variables
"""
Different Variable Naming Conventions:: 
-Variable name starts with alphabet not with number. e.g. follow
-No space in between variable name e.g. follow them
-Underscore can be used in between e.g. follow_them
-Shouldnot start with number e.g. 1follow

"""
s= "Yes"
print(s)

s1 = 20
print(s1)

s_t = 4
print(s_t)

_s = 11
print(_s)

#data types list
'''
-Numeric (Integers, Float, Complex Numbers)
-Sequence Type (String, List, Tuple)
-Dictionary
-Set
'''
"""
1. Mutable Data Types : which can be changed or updated
        (List, Dictionary, Byte Array)
2. Immutable Data Types : which cannot be changed or updated
        (Int, Float, Complex, String, Tuple, Set)
"""
s=1
print(s, "is of type", type(s))

t=2.0
print(t, type(t))

u=1+5j
print(u, "is of type", type(u))

c = "hey beautiful people"
print(c, type(c))

d = ''' 
        Nice to meet you all
        Hope to see you again
'''
print(d) #string in multiple line
u= [89,'move', 1.1] #list is mutable
u[1]=11
print(u,type(u))

t= (10,"Goodbye", 60)
print(t, type(t)) #tuple is immutable :cannot be added, deleted,
# updated : so it is fast in comparison to list

#Datatype Conversion
'''
-process of converting the value of one data type(int, str,float)
to another data type.
Two types of conversion:
1. Implicit Type Conversion
2. Explicit Type Conversion
'''
#Explicit type conversion
num_int = 123
num_str = "111"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before type casting:", type(num_str))

num_str = int(num_str) #converting string to integer
print("Data type of num_str after type casting:", type(num_str))

num_sum = num_int + num_str

print("sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))

#Implicit Type Conversion
num_int = 123
num_flo = 1.23

num_new = num_int +num_flo

print("Data type of num_int:", type(num_int))
print("Data type of num_flo:", type(num_flo))

print("Data type of num_new:", num_new)
print("Data type of num_new:", type(num_new))

#Q1. WAP to print a your name.
print("Anshika Bhattarai")

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

number = int(input("Enter a number : "))
square = number ** 2
print("Square of the given number is : ", square)
