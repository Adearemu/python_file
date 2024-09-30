# This program ask users for their user name and password

print("Enter your name")
name = input()

print("Kindly enter your username " + name)
username = input()

print("Kindly enter your password " + name)
password = input()

if password == "Paiko1606" and username == "Big Boss":
    print("You are welcome " + name)

elif password == "Tesco123" and username == "Tesco Malaika":
    print("You are partially welcome " + username)    

else:
    print("You are an anonymous hacker")