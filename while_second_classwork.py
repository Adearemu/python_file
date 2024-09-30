# This program continuously ask for your password

print("Enter your name")

name = input()

while True:
    print("Enter your password")
    password = input()
    if password == "Paiko1606":
        break

print("Thank you for providing your password", name)