# String slicing
"""
mystr = "Kiran is a good boy"
"""
# to print length of an string use len.
"""
print(len(mystr))
print(mystr[0:19])
"""
# There is a rule in str slicing that  if you include 0:4 then it does not print Kiran it will print Kira only 
# to print kiran you need to include 0:5
# also know that 0 is including and 4 is excluding
"""
mystr = "Kiran is a good boy"
print(mystr[ ::-2])
"""
# positive number is counted from the start and negative number is counted from the end of the string

mystr = "Kiran is a good boy."
print(mystr.isalnum())
print(mystr.isalpha())
# both isalnum and isalpha functions check weather it is  an alpha numeric or not 
# and it's answer is in boolean

print(mystr.endswith("bdoy"))
# endswith function check that weather it ends with the given value i mean string or not
# and it also answers in boolean

print(mystr.count("a"))
# count function check for the number of given value in the string

print(mystr.capitalize())
# capitalize function capitalize the first letter of a string

print(mystr.find("is"))
# find function finds the index of the given value

print(mystr.lower())
# lower function lower all the cases in the string

print(mystr.upper())
# upper function upper all the cases in the string

print(mystr.replace("is", "are"))
# it replaces the value with the given value