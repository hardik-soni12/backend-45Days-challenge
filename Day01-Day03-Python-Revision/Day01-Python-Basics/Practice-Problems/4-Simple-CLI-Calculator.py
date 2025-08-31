# Simple CLI Calculator

'''Question:

Write a program that asks the user for two numbers and an operation (+, -, *, /),
then prints the result of that operation on those numbers.
Example Input:
First number: 10
Second number: 4
Operation: *
Expected Output: 40
'''

def calculate():
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        operation = input("Enter the operation (+, -, *, /): ")

        result = 0

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation.")
            return

        
        print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculate()
