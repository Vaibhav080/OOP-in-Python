# We will now create a data type for handling fraction

class Fraction:
    
    def __init__(self, n, d):
        self.num = n
        self.den = d
    
    # for print function
    def __str__(self):
        return "{}/{}".format(self.num, self.den) # we use string formatting here
    
    # add magic method when + is used
    def __add__(self, other):
        temp_num = self.num*other.den + other.num*self.den
        temp_den = self.den * other.den
        
        return "{}/{}".format(temp_num, temp_den)
    
    # Similarly can be done for sub, mul and div using __sub__, __mul__, __truediv__
    # To read more on this you can read https://www.geeksforgeeks.org/python/dunder-magic-methods-python/
    
x = Fraction(3, 4)
y = Fraction(5, 6)
    
print(x)
print(y)
print(x+y)