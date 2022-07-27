# Dict = {"Kiran": "Programmer", "Saurav Rai": "Hacker", "Dipika": {"As a": "Friend only", "Sometime\s as a": "close friend", "Sometime'\s as a ": "May be girlfriend"}}
# print(Dict["Dipika"]["As a"])
# print(Dict.items())

# Question: Create a dictionary and take input from the user and return the meaning of the word from the dictionary

# D = {
#     "Kiran": '53kg',
#     "Anil": '65kg',
#     "sunil": '55kg',
#     "saurav": '50kg'
# }

# name = input("Enter your name to get your weight")
# print(D[name])


# set in python
# l = [1,2,3,4]
# s_from_list = set(l) 
# print(type(s_from_list))

# method to add a items in set
# s = set()
# s.add(1) 
# print(s)



# if else statement

# var1 = 3
# var2 = 5 
# var3 = input()

# if var3>var2:
#     print("Greater")
# else:
#     print("Lesser")

# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
#

print("Enter 1st numbet")
num1 = int(input())
print("Enter 2nd number")
num2 = int(input())
print("Choose your operator '+' +,-,/,%,*")
num3 = input()

if num1 == 45 and num2 == 3 and  num3 == '*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3 == '*':
    num4 = num1 * num2
    print(num4)
elif num3 == '+':
    ADD = num1 + num2
    print(ADD)
elif num3 == '/':
    Dev = num1 / num2
    print(Dev)
elif num3 == '-':
    Sub = num1 -num2
    print(Sub)
elif num3 == '%':
    per = num1 % num2
    print(per)
else:
    print("Error please check your input ")



    
    
