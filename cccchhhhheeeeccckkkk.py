# This program does not bring error if you input string instead of intergers

print("Enter your name")

name = input()


try:
    print("Enter your number",name)
    num = int(input())
    if num % 2 == 1:
        print("It is an odd number")
    else:
        print("It is even number")
except ValueError:
    print("You did not input any number")