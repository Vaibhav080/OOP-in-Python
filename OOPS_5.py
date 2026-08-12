# Inheritance reverse inheritance from child to parent is not allowed
# child class object cannot access hidden attribute from parent
# Method Overiding, Method Overloading, Operator Overloading => Polymorphism

class User:
    
    def login(self):
        print("Login")
    
    def register(self):
        print("Register")
        
class Student(User):
    def enroll(self):
        print("Enroll")
        
    def review(self):
        print("Review")
        
stu1 = Student()

stu1.login()
stu1.enroll()
stu1.review()
stu1.register()

class Parent:
    def __init__(self, num):
        self.__num = num
    def get_num(self):
        return self.__num
    
class Child(Parent):
    def show(self):
        print("This is child class")
        
son = Child(100)
print(son.get_num())
son.show()

# Types of Inheritance

# 1) Single Level Inhertitance : one parent class one child class
# 2) Multi Level Inheritance : one grandparent class one parent class and one child class
# 3) Heirarchial Inheritance : one parent and multiple children
# 4) Multiple Inheritance : one child and multiple parents (not in java only in python)
# 5) Hybrid Inheritance : Combination of above inheritance

# MRO - Method Resolution Order

# polymorphism - Method Overriding ; Method overloading ; Operator Overloading


