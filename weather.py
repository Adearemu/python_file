# This program ask about weather

print("Hello World")

print("I'm about to ask about weather condition")

print("Please, enter your name")

name = input()

print("Please input your weather condition {Rainy, Cloudy, Sunny and Fair}",name, ".")

weather = input().capitalize()

if weather == "Rainy":
    print("Wow, it is rainy, ",name ,"please use a rain coat")
elif weather == "Cloudy":
    print("I will advise to get home quickly because it might rain soon")
elif weather == "Sunny":
    print("Go out with your sunscreen because it is very sunny")
elif weather == "Fair":
    print("The weather is in good condition, so you can go out with whatever you want")
else :
    print("You did not input any weather condition")

print("Thank you for your cooperation, ", name)


