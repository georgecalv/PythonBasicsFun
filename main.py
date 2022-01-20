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




# # GETTING USER INPUT
# print("Enter your favourite number")
# fav_number = input()
# print(type(fav_number))
# print("Your favourite number is", fav_number)
# print("Your favourite number doubled is", fav_number * 2, sep = "*")
# print("hello" * 2, end = "~~~~~~~") # sep and end are called keyword arguments
# print("here")
# # Really wnat to double fav number
# # convert fav number string to integer or float
# # this is called type conversion
# fav_number_int = int(fav_number)
# print("Your favourite number doubled is",fav_number_int * 2)



# FORMATTING (decimal numbers)
# few ways to do this
# 1. c style
print(math.pi)
# round to two decimal places
print("%.2f" %(math.pi))
# 2. Pythonic way
print("{:.2f}".format(math.pi))
# 3. built in function round
# round() rounds number and can be stored as such
print(round(math.pi, 2))




# CONDITIONALS (if statements)
# if some condition is true (boolean)
#   then execute some code (if statement body)
x = 7
if(x == 6):
    print("x equals 6")
    # this is the body
    # body only executes if x is equal to 6
    # the boolean is true
    # note standard indentation is one tab or 4 spaces
# executes when preceding if is false
elif(x == 7):
    print("x isnt 6 but it is 7")
else:
    print("x is not 6")
x = 5
if (x < 0):
    print("x is neagative")
elif(x > 0):
    print("x is positive")
else:
    print("x is 0")

# LOOPS
# repeat statments
# for loops and while loops 
# for loop structure
# for item in sequence:
    # body satements to repeat
# many dif sequences
# lists are sequences
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
# strings are sequences
for character in "gonzaga":
    print(character, end = "*")
print("")
# generate our own sequences
# built in with range() generates a sequence
# range(9) generates sequence starts at [0,9)
for i in range(9):
    print(i, end = " ") 
print()
# range(start, stop), [start, stop)
# range(start, stop, step), [start, stop) going up in step
for i in range(4,9):
    print(i, end=" ")
print()

# task 1 
for i in range(8, 3, -2):
    print(i, end=" ")
print()

# task 2
for j in range(0,21,2):
    print(j, end=" ")
print("")

# task 3
for y in range(2, 42, 2):
    if(y == 40):
        print(y)
    else:
        print(y, end=", ")



# Functions
# reduce amount of redundant code
# write once call multiple times
# helps with code organization








