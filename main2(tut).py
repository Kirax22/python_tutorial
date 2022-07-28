# Lists in python
"""
grocery = ["harpic","vim bar", "deorant","Bhindi","lolipop", 56]
print(grocery[2])
"""
"""
numbers = [1,4,5,24,3.5]
"""
# numbers.sort() it sorts the value from the start small number to large number
# numbers.reverse(11)it reverse the number from last to first
"""
print(numbers[0:5:2]) 
"""
# print(len(numbers)) it is used to get the length of a list
# print(min(numbers)) it is used to get the minimum value of the list
# print(max(numbers)) it is used to get the maximum value of the list
# first value is (including index). (second value is excluding index) and (last value is extending index)
# numbers.append(2) it is used to append the value in the list as many time as you can
# numbers.insert( 2, 9) it is used to insert the value in the list wherever you want as long as you set the appropriate index on it
# numbers.remove(4) it is used to remove the value in the list any value
# numbers.pop() it is used to chop off the value at the last of the list
# numbers[1] = 98 this technique is used to change the value of the list according to your need
"""
print(numbers)
"""
# Tupple in python

# Mutable = can change(list is mutable)
# Immutable = cannot change(tupple is immutable)

# when you create tupple don't forget to use comma or else it won't be created as a tupple
"""
tp = (1,2,3)
print(tp)
"""
a = 1
b = 8
# Traditional way to swap the value
var = a
a = b
b = var
print(a,b)
# new way in python
"""
x = 3
y = 4
x, y = y,x
"""