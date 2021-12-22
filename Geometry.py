# In VS Code, create a module titled geometry and add two functions in there. 
# One that will calculate the area of a circle given a radius. 
# The second will find the hypotenuse of a right angle given the two sides. 
#Import the module or the functions from the module and use it to find the answers to the below questions
from math import pi, sqrt
def circle(radius):
    return pi * radius **2




# # What is the hypotenuse of a right angle with sides of 3in and 4in?
def right_angle(a, b):
    return sqrt(a**2 + b**2)
