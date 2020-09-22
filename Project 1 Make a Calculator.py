#This python program will be a better calculator than the basic calculator.

#You can convert whatever a user inputs by putting float or int in front of the string.
#Ask user to input first number.
num1 = float(input("Enter first number: "))

#User chooses what operator to use.
op = input("Enter operator:  ")

#Ask user to input second number.
num2 = float(input("Enter second number: "))

#Check to see what operator the user chooses
##If the user does not input an operator the result is invalid.
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")