# What is OOPS. It is a different way of writing code like in python you # cannot use upper with list as list object has no attribute upper similarly append
# Everything is an object in python.

# Generality to Specificity

# Class is a blueprint. Object is of a class. like a= 2 is a object of class int
# Class contains data or property and functions or behaviour

# Basic structure of class
class Car: # Name of class should be in pascal case  ThisIsPascalCase
    #Camel case thisIsCamelCase
    #Snake case snake_case
    color = "blue" # data
    model = "sports" # data
    
    def calculate_avg_speed(km, time): # variable name and function name should be in snake case
        # Some code
        pass
    
# Class can be represented diagramatically by check pictures

# Object Examples

# Car = Fortuner
# Game = GTA 6

# We can also create an object by object literal for built in classes in python

# Lets make a class for a real world example like ATM machine using OOP

# Functions vs Methods

# Methods are function written inside a class

# Functions are for all classes

# init is a constructor. Constructor is a special method whose code is automatically executed when we create an object of the class.
# constructor is a special/magic/dunder methods. Magic methods are special methods which are automatically triggered.
# User does not has control of it
# self is the current object you are working on.
# why class's method need object using self

# Encapstulation using access modifiers. We hide the instance variable or method using __ after.
# Encapstulation is needed we need to protect our data so that invalid access can be prevented
# Nothing in python is truly private
# First I will hide my data and if he want to see it then he can see via get and can set only by my rules.

class ATM:
    # static variables are defined outside constructor
    
    __counter = 1
    def __init__(self):
        self.__pin = "" # Instance variable are variables which have different values for different objects
        self.__balance = 0
        self.sno = ATM.__counter
        ATM.__counter = ATM.__counter + 1
        
        self.__menu()
        
    def __menu(self):
        user_input = input("""
                           Hello, How would ypu like to proceeed?
                           1. Enter 1 to create PIN.
                           2. Enter 2 to deposit.
                           3. Enter 3 to withdraw.
                           4. Enter 4 to check balance.
                           5.Enter 5 to exit.
                           """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Thank You!")
            
    @staticmethod      
    def get_counter():
        return ATM.__counter
    
    def set_counter(new):
        if type(new) == int:
            ATM.__counter = new
        else:
            print("Not Allowed")

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if(type(new_pin) == str):
            self.__pin = new_pin
            print("PIN Changed")
        else:
            print("Not Allowed")
    
    def create_pin(self):
        self.__pin = input("Enter your PIN: ")
        print("PIN set successfully.")
        
    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance = self.__balance + amount
            print("Deposit Successful")
        else:
            print("Invalid PIN")
        
    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount<self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw Successful!")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid PIN")
                
    def check_balance(self):
            
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid PIN")
                
sbi = ATM()
sbi.create_pin()
sbi.deposit()
sbi.withdraw()
sbi.check_balance()
print(sbi.get_pin())
sbi.set_pin(2000)

# Reference Variable sbi = ATM() sbi here is reference variable which is pointing to the object at a specific memory location
# Static Two type of variable : Instance Variable(its a variable for which value is different for every object); class variable(value is same for all variable)

# Relationship between classes : Aggregation (has a relationship) ; Inheritance (is a relationship)
# Customer has a address ; smartphone is a product ; car is a vehicle

# Inheritance while creating udemy website both student and mentor are student and require login and registration so we can use it under class user and student and mentor can inherit its method

# In inheritance we inherit data members, member functions, constructor, private members are not inherited

