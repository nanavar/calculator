x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

operation = input("Choose math operation (+, -, *, /,): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Error. You didn't follow the rules. Try again.")
