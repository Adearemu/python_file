# This calculate the area and perimeter of a circle

print("What will you calculate between the circumference and area of a circle")

pi = 22/7

result = input().capitalize()
if result == "Area of a circle":
    print("Enter your radius in cm")
    radius = int(input())
    area = pi * (radius ** 2)
    print("The area of a circle with radius", radius, "is " + str(round(area, 2)) + "cm²")
elif result == "Area":
    print("Enter your radius in cm")
    radius = int(input())
    area = pi * (radius ** 2)
    print("The area of a circle with radius", radius, "is " + str(round(area, 2)) + "cm²")
elif result == "Circumference of a circle":
    print("Enter your radius in cm")
    radius = int(input())
    circumference = 2 * pi * radius
    print("The circumference of a circle with radius", radius, "is " + str(round(circumference, 2)) + "cm²")
elif result == "Circumference":
    print("Enter your radius in cm")
    radius = int(input())
    circumference = 2 * pi * radius
    print("The circumference of a circle with radius", radius, "is " + str(round(circumference, 2)) + "cm²")