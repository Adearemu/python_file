list_of_colors = ["blue", "red", "white", "purple", "green", "yellow", "black", "pink"]

print(list_of_colors.index("yellow"))

print(list_of_colors.index("blue"))


list_of_colors.append("brown")

print(list_of_colors)

list_of_colors.insert(5, "indigo")

print(list_of_colors)

name = "sabur"

#name.append("i")

print(name)

list_of_numbers = [10, 2, 4, 5, 6, 86, 8554, 98, 46, 6546, 100]

list_of_numbers.sort()

print(list_of_numbers)

list_of_numbers.sort(reverse=True)  # allows it to run from highest to lowest

print(list_of_numbers)

list_of_colors.sort()
print(list_of_colors)


alpha = ["a", "A", "Z", "z", 'b','B']

alpha.sort() # small letter has higher precendent than capital letter

print(alpha)

alpha.sort(key=str.lower)  # recogniize everything as a small letter
print(alpha)

list_of_colors.remove("pink")

list_of_colors[0] = ""

print(list_of_colors)