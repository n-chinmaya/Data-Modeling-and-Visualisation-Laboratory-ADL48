def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    choice = int(input("Choose operation (1-Add, 2-Subtract, 3-Multiply, 4-Divide): "))
    
    if choice == 1:
        result = a + b
    elif choice == 2:
        result = a - b
    elif choice == 3:
        result = a * b
    elif choice == 4:
        result = a / b
    else:
        result = "Invalid choice"

    print("Result:", result)

if __name__ == "__main__":
    main()