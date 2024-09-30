# This is a simple calculator

def calculator():
    """This is a basic calculator"""
    print("This is a basic calculator")

    
    try:
        print ("Enter your first number")
        first_num = int(input())
        print("Enter your second number")
        second_num = int(input())
    except ValueError:
        print("You are  asked to type a number")
        

    try:

        print("Choose an operation between these four operations")
        print("1 = addition")
        print("2 = subtraction")
        print("3 = division")
        print("4 = mutiplication")

        print("Enter your operation")
        operation = int(input())

        if operation == 1:
            answer = first_num + second_num
            print("The addition of " + str(first_num)+ " and " + str(second_num) + " is " + str(answer))
        elif operation == 2:
            answer = first_num - second_num
            print("The subtraction of " + str(first_num)+ " and " + str(second_num) + " is " + str(answer))
        elif operation == 3:

            try:
                print(first_num / second_num )
                
            except ZeroDivisionError:
                print("You cannot divide by zero")
        elif operation == 4:
            answer = first_num * second_num
            print("The mutiplication of "+ str(first_num)+ " and " + str(second_num)+ " is "+ str(answer))
        else:
            print("You enter an invalid operation")
    except ValueError :
        print("You are asked to choose an operation with interger not with strings")
    except UnboundLocalError:
        print("You are asked to write an interger for the operation")
    
    again = input("Do you want to perform another operation: ").lower()
    if again == "yes":
        calculator()
    else:
        print("Goodbye")



calculator()

# def calculator():
#     """A basic calculator for addition, subtraction, multiplication, and division."""
#     print("This is a basic calculator")

#     while True:
#         try:
#             # Get input from the user
#             print("Enter your first number:")
#             first_num = float(input())
#             print("Enter your second number:")
#             second_num = float(input())

#             # Get the operation from the user
#             print("\nChoose an operation:")
#             print("1 = Addition")
#             print("2 = Subtraction")
#             print("3 = Division")
#             print("4 = Multiplication")
#             print("Enter your choice (1, 2, 3, or 4):")
#             operation = int(input())

#             # Perform the chosen operation
#             if operation == 1:
#                 answer = first_num + second_num
#                 print(f"The addition of {first_num} and {second_num} is {answer}")
#             elif operation == 2:
#                 answer = first_num - second_num
#                 print(f"The subtraction of {first_num} and {second_num} is {answer}")
#             elif operation == 3:
#                 if second_num == 0:
#                     print("Error: Cannot divide by zero")
#                 else:
#                     answer = first_num / second_num
#                     print(f"The division of {first_num} by {second_num} is {answer}")
#             elif operation == 4:
#                 answer = first_num * second_num
#                 print(f"The multiplication of {first_num} and {second_num} is {answer}")
#             else:
#                 print("Invalid operation. Please choose a number between 1 and 4.")

#         except ValueError:
#             print("Invalid input. Please enter numeric values for numbers and a valid integer for the operation.")
#         except ZeroDivisionError:
#             print("You cannot divide by zero. Please enter a non-zero value for the second number.")

#         # Ask if the user wants to perform another operation
#         again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
#         if again != "yes":
#             print("Goodbye!")
#             break

# # Run the calculator function
# calculator()
