# Functions 
def add_numbers(p, q):
    return p + q

def subtract_numbers(p, q):
    return p - q

def multiply_numbers(p, q):
    return p * q

def divide_numbers(p, q):
    if q == 0:
        return "Error: Division by zero is not allowed"
    return p / q

# input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nChoose the operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

# Performing 
if choice == '1':
    result = add_numbers(num1, num2)
elif choice == '2':
    result = subtract_numbers(num1, num2)
elif choice == '3':
    result = multiply_numbers(num1, num2)
elif choice == '4':
    result = divide_numbers(num1, num2)
else:
    result = "Invalid choice"

print("\nResult:", result)
print("Thankyou for using me!")