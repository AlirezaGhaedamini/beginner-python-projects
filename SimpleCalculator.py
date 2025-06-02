print("🧮 Welcome to the Simple Calculator")

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
operation = input("Enter the operation (+ , * , / , - ) : ")

if operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation == "*":
    print(first * second)
elif operation == "/":
    print(first / second)
else:
    print("Invalid operation. Please enter a valid operation.")