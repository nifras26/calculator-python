def calculator():
    n= float(input("Enter first number: "))
    s= float(input("Enter second number: "))
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input("Enter choice (1/2/3/4): "))
    if operation == 1:
        print(f"The result is: {n + s}")
    elif operation == 2:
        print(f"The result is: {n - s}")
    elif operation == 3:
        print(f"The result is: {n * s}")
    elif operation == 4:        
        print(f"The result is: {n / s}")       
    else:
        print("Invalid operation")
if __name__ == "__main__":        
    calculator()