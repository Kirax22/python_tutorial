# Variables casting
"""
a = int(20)
b = str(20)
c = float(20)

print(a,b,c)
"""
# many values to multiple variables
"""
x,y,z = "Kiran Rai","saurav rai","dipika tamang"
print(x,y,z)
"""
# 1 value to multiple variables
"""
x = y = z = "You"
print(y)
"""
# Unpacking the collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the variables. This is called unpacking.

# Example~:
"""
fruits = ["apple","banana","cherry"]
x,y,z = fruits

print(x)
print(y)
print(z)
"""
# Did you get this first tupples were created and then assigned to many values to multiple variables x,y,z and at last you can get the output/result by printing the variable name

# Python string slicing

# Slicing
# you can return a range of characters by using slice syntax. Specify the start index and the end index, seperated by a colon, to return a part of the string

var = "This is Kiran Rai,. Who am I talking to?"
print(var(7:11))