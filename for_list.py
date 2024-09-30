for i in range(4):
    print(i)



for i in [0, 1, 2, 3]:
    print(i)


list_of_colors = ["blue", "red", "white", "purple", "green", "yellow", "black", "pink"]

for color in list_of_colors:
    print(color)

for i in range(len(list_of_colors)):
    print("The value of index " + str(i) + " is " + list_of_colors[i]) 


colorBlue, colorRed, colorWhite, colorPurple, colorGreen, colorYellow, colorBlack, colorPink = list_of_colors

print(colorBlack)
print(colorYellow, colorBlack)


blue, white, red, purple = "blue", "white", "red", "purple"

a = "AAA"
b = "BVB"

a, b = b, a

print(a)
print(b)