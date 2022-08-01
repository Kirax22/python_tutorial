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
# string slicing
# String slicing return the characters falling between indices n and m
# String at n, n+1,n+2...till m-1. The syntax is:
#   Here n = size of the list  
    # string[Start:End:Step_value(Skipping value)]
# last index is to skip
"""
str1 = "My name is Kiran Rai"
print(len(str1))
print(str1[::-2])
"""

# list data type in python
# list is a collection of different values or different types of items.
# unlike array in c/c++/java a list is capable of storing different types of values under one roof.
# The list in the list are seperated with the comma(,) and enclosed in square bracket[].
# List provides us the facility to store multiple types of values in a single unit.
# There is two types of indexing:
# Forward indexing
# and Backward indexing
# You can update the value of any list using 

# Example practice

# list = ["Kiran", "Rai", "Is", "A", "Hacker", 1 ,1 ,22,23,43,32]
# print(list[:3:-1])

# we can also put list inside list aka 2dlist,3d list and so on....
 
# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# for sublist in list1:
#     for i in sublist:
#         print(i) 
# print(type(list1))

# list2 = [
#     [1,2,3,],[5,6,7],[8,9,0]
# ]
# list2.insert([1],[1],4)
# print(list2)
"""

list3 = [1,2,3,4,5,7,8]
list3.clear()
print("""

# Dictionary
# A dictionary is a collection which is unordered, changeble and indexed. In python dictionaries are written within curly brackets, and they have keys and values. Means the dictionary contains two things first is the key and second is value.
"""
dict1 = {'Kiran': "Rai", 'Dipika': "Tamang",} 
for x in dict1.values():
    print(x)
"""
# change value of dictionary

dict1 = {'Kiran': "Rai", 'Dipika': "Tamang",} 
dict1['Dipika'] = 'Rai'
print(dict1)
