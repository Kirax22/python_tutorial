# var1 = 54
# var2 = 34
# var3 = int(input())
# if var3 > var2:
#     print("Greater")
# elif var3 == var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [1,2,3,4,5]
# print(52 in list1)
# if 4 in list1:
#     print("Yes, num 4 is in the list")

# list2 = [2,1,4,5,6]
# print(1 not in list2)
# if 3 not in list2:
#     print("No, 3 is not in the list2")


# age = int(input("Enter your age:"))
# if age in range(7,100):
#     age = int(input("Enter your age:"))
# elif age < 18:
#     print("We are sorry to inform you that you cannot drive sir/mam")
# elif age  == 18:
#     print("We will think about it")
# else:
#     print("Yes, you can drive")

# Exercise 2 Faulty calculator

# Design a calculator  which will correctly  solve all the problems except the following ones:
# 45 * 3 = 555, 56 + 9 =77, 56/6 = 4
# your operator should take operator and the numbers as input from user and then return the result

print("Enter the first Number")
num1 = int(input())
print("Enter the second Number")
num2 = int(input())
print("So what you want? " + '+.-,/,*,%')
num3 = input()

if num1 == 45 and num2 == 3 and num3 == '*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3 == '*':
    num4 = num1 * num2
    print(num4)
elif num3 == '+':
    plus = num1 + num2
    print(plus)
elif num3 == '/':
    Dev = num1 / num2
    print(Dev)
elif num3 == '-':
    Sub = num1 - num2
    print(Sub)
elif num3 == '%':
    percent = num1 % num2
    print("Your result is " ) + int(( percent))
else:
    print("Error! please check your input")