class Geometry:
    def area(self, radius):
        return 3.14*radius*radius
    def area(self, l, b):
        return l*b
    
obj = Geometry()
print(obj.area(4))

#Error

# Method Overloading means one method with different input behave differently
# It does not exist in Python but can be implemented with if statements and default values

# Operator Overloading : like + can be used for string concatenation other than addition 
# Operator Overloading is achieved via magic functions.
