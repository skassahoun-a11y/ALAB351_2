# simple_calculator.py

# 1. Get two numbers from the user
print("Welcome to the Simple Calculator!")
print("You can perform addition, subtraction, multiplication, and division.")
print("----------------------------------------------------")
print()
num1_input = input("Enter the first number: ").strip()
num2_input = input("Enter the second number: ").strip()

# 2. Validate that the inputs are valid numbers (including decimals and negatives)
# Removing a leading '-' and one '.' lets .isdigit() check floats and negative numbers safely
is_valid_num1 = num1_input.lstrip("-").replace(".", "", 1).isdigit()
is_valid_num2 = num2_input.lstrip("-").replace(".", "", 1).isdigit()

if not (is_valid_num1 and is_valid_num2):
    print("Error: Please enter valid numeric values.")
else:
    # Convert the validated strings into floating-point numbers
    num1 = float(num1_input)
    num2 = float(num2_input)

    # 3. Ask the user to choose an operation
    operation = input("Choose an operation (+, -, *, /): ").strip()

    # 4. Perform the calculation and print the result
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        # Check for division by zero before dividing
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Unsupported operation. Please choose +, -, *, or /.")