# This is my first python simple calculator from CWH python tutorial
 
print("Print your first number")
num1 = int(input())
print("Print your second number")
num2 = int(input())
print("Choose your operator")
num3 = input()

# conditions
# 50 * 50 = 5
# 50 - 50 = 6
# 50 + 50 = 7
# 50 / 50 = 8
# 50 ** 50 = 9
# 50 % 50 = 10

if num1 == 50 and num2 == 50 and num3 == '*':
    print("5")
elif num1 == 50 and num2 == 50 and num3 == '-':
    print("6")
elif num1 == 50 and num2 == 50 and num3 == '+':
    print("7")
elif num1 == 50 and num2 == 50 and num3 == '/':
    print("8")
elif num1 == 50 and num2 == 50 and num3 == '**':
    print("9")
elif num1 == 50 and num2 == 50 and num3 == '%':
    print("10")
elif num3 == '*':
    num4 = num1 * num2
    print(num4)
elif num3 == '-':
    sub = num1 - num2
    print(sub)
elif num3 == '+':
    plus = num1 + num2
    print(plus)
elif num3 == '/':
    div = num1 / num2
    print(div)
elif num3 == '**':
    exp = num1 ** num2
    print(exp)
elif num3 == '%':
    per = num1 % num2
    print(per)
else:
    print("please check your input")