first_number = float(input("What is your first number?: "))
second_number = float(input("What is the second number?: "))
operation = input("What is the operation? (input plus, minus, times, divide or remainder): ")
if operation == "plus":
    print(first_number+second_number)
elif operation == "minus":
    print(first_number-second_number)
elif operation == "times":
    print(first_number*second_number)
elif operation == "divide":
    print(first_number/second_number)
elif operation == "remainder":
    print(first_number%second_number)
else:
    print("Invalid!")