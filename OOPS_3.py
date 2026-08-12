# Pass by reference
# Class objects in Python are mutable like list, dictionary, sets

class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name, "sir")
    else:
        print("Hello", customer.name, "ma'am")        

cust = Customer("Vaibhav", "Male")
print(cust.name)
greet(cust)

# Collection of objects: we can use objects inside list, dictionary, tuples

class Customer:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
c1 = Customer("ABC", 22)
c2 = Customer("XYZ", 24)
c3 = Customer("PQR", 26)

L = [c1, c2, c3]

for i in L:
    print(i)
    print(i.name, i.age)