a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division"))

if choice == 1:
    print("Addition of two numbers is: ", a+b)
elif choice == 2:
    print("Subtraction of two numbers is: ", a-b)
elif choice == 3:
    print("Multiplication of two numbers is: ", a*b)
elif choice == 4:
    print("Division of two numbers is: ", a/b)
else:
    print("Invalid choice")

# match choice:
#     case 1:
#         print("Addition of two numbers is: ", a+b)
#     case 2:
#         print("Subtraction of two numbers is: ", a-b)
#     case 3:
#         print("Multiplication of two numbers is: ", a*b)
#     case 4:
#         print("Division of two numbers is: ", a/b)
#     case _:
#         print("Invalid choice")