# Dictionaries
# A dictionaries is a collection of many values
# Dictionaries are a representation of key value pairs


mycat = {"size": "fat", "color": "white"}

size_of_my_cat = mycat["size"]
colorOfMyCat = mycat["color"]

cars = {"brand": "lexus", "model": "IX-250"}

print("I have a " + cars["brand"] + " of " + "model " + cars["model"])

countries = {
    "France" : "Paris",
    "Japan" : "Tokyo",
    "Canada" : "Ottawa",
    "Mongolia" : "Ulaanbaantaar"
}

capital_of_mongolis = countries["Mongolia"]

print(capital_of_mongolis)

school = {
    "class" : "SS1"
}

numbers = {
    "number1": 1,
    "number2": 2,
    "list1": [0, 1, 2, 3, 4],
    "dict1": {"one": 1, "two": 2}
}

animals = ["Goat", "Lion", "Chimpazee", "Gorilla", "Python"]

python = animals[4]

print(size_of_my_cat, colorOfMyCat)
print(countries)

countries["Nigeria"] = "Abuja"

countries["Usa"] = "Washington DC"

print(countries)

print(list(countries.items()))


print (list(countries.keys()))

for key in list(countries.keys()):
    print("This is country", key)

for capital in list(countries.values()):
    print(capital)

for country, capital in countries.items():
    print("The capital of " + country + " is " + capital)

# keys() # values() # items() 

#create a product dictionary, in that product that product is going to be a list