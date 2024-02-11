"""class Phone: #creating phone class
    def make_calls(self): #inbuild parameter ko object sanga invoke
        # garnu xa vawney we will use self.
        print("Hello, calling my cell phone number two.")
    def play_games(self):
        print("I am playing a game very well.")

p1 = Phone() #instantiating the p1 object :: phone class ko object create gawreyko
p1.make_calls() #class ko method ko invoke gawrey ko
p1.play_games()

#adding extra parameter other than self

class Phones:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def set_battery(self,battery):
        self.battery=battery
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def show_battery(self):
        return self.battery
    def make_calls(self):
        print("hello, lets make a call")
    def play_gaming(self):
        print("we are playing")

p2 = Phones()
p2.set_color("Yellow")
p2.set_cost(1000)
p2.set_battery("Great")

p2.show_color()
p2.show_cost()
p2.show_battery()
p2.make_calls()
p2.play_gaming()"""

#using constructor:

"""class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_employee_details(self):
        print("Name of employee is ", self.name)
        print("Age of employee is ", self.age)
        print("Salary of employee is ", self.salary)
        print("Gender of employee is ", self.gender)

e1 = Employee('Anshika',22,100000,'Female')
e1.show_employee_details()"""

"""class Rabbit:
    def __init__(self,name,color,teeth,age,food,number):
        self.name = name
        self.color = color
        self.teeth = teeth
        self.age = age
        self.food = food
        self.number = number

    def show_rabbit_details(self):
        print("Name of the rabbit", self.name)
        print("Color of rabbit", self.color)
        print("Teeth structure of rabbit", self.teeth)
        print("Age of rabbit", self.age)
        print("Food eating by rabbit", self.food)
        print("Number of rabbits in my house", self.number)

r1 = Rabbit('Kaharayo','White','Protude',5,'Carrot',12)
r1.show_rabbit_details()

class Person:
    def __init__(self,who,how,address):
        self.who = who
        self.how = how
        self.address = address

    def show_person_detail(self):
        print("Who is this person", self.who)
        print("How are you in person")
        print("Where do you live")
p1 = Person('I am humamn being','I am doing great','i live in my sweet home')
p1.show_person_detail()"""

#INHERITANCE

class Plants:
    def __init__(self,type,habitat,number):
        self.type = type
        self.habitat = habitat
        self.number = number
    def show_plants_details(self):
        print("Type of plant ", self.type)
        print("Habitat ", self.habitat)
        print("Number of plants", self.number)

p1 = Plants('Trees','Terai',10)
p1.show_plants_details()

class Pine(Plants):
    def show_pine_details(self):
        print('I am pine tree among plants')

p2 = Pine('Green Tree','Hilly',1)
p2.show_plants_details()
p2.show_pine_details()
