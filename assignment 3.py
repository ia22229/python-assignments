#a =int(input("Please choose operation: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
b = int(input("Please enter first number: "))
c = int(input("Please enter second number: "))
a= input("+ for addition, \n- for subtraction, \n* for multiplication, \n/ for division: \nPlease choose operation:")
if a == "+":
    print("The result of addition is: ", b + c)
elif a == "-":
    print("The result of subtraction is: ", b - c)
elif a == "*":
    print("The result of multiplication is: ", b * c)
elif a == "/":
    if c != 0:
        print("The result of division is: ", b / c)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
