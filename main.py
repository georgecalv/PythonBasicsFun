# put all import statemnets at the top
import math
# this is a one line comment 
# a comment is code that is ignored by python
# use comments to document code

"""
this is a block comment
multiple line comments
multi lines brother

"""

print("hello world")

# VARIABLES
x = 5 # read this as "x is assigned 5" or x stores 5
# Not "x equals 5"
#variable stores a value
# a value has a data type 
# a data type defines a range of values
# example: the int data type (short for integer): represent whole numbers
print(type(x)) 
#shows type of variable
x = 5.5
print(x)
print(type(x))
# float data type represents numbers with fractionable parts(AKA decimals)
x = "Hello"
print(x)
print(type(x))
# str or string represents a certain sequence of characters 
x = "5"
print(x)
print(type(x))
# is a string not an integer


# OPERATERS
# PEMDAS
    # parens, exponents, multiplication, division, addition, subtraction
# * = multiply
print(4 * 5)
# / floating point division (NORMAL division)
print(5 / 2)
# // integer division (the whole number result of flaoting point division)
print(5 // 2)
# ** exponentiation AKA power
print(2 ** 5) # if you have multiple in an expresion you evaluate right to left

# we can also use the pow() function from the math module 
# need to import math module
# .py file is known as a module or script 

# print 2^5 
# pow function results in a float
print(math.pow(2,5))




# GETTING USER INPUT
print("Enter your favourite number")
fav_number = input()
print(type(fav_number))
print("Your favourite number is", fav_number)
print("Your favourite number doubled is", fav_number * 2, sep = "*")
print("hello" * 2, end = "~~~~~~~") # sep and end are called keyword arguments
print("here")


