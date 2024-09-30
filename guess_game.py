# The program ask user to guess a number correctly
import random

print("Enter your name")

name  = input()

print("You are asked to guess a number " + name)

num = random.randint(1, 20)

for trial in range(1, 6):
    print("Guess the number")
    guess = int(input())
    if guess < num:
        print("The number is low")
    elif guess > num:
        print("The number is high")
    elif guess == num:
        print("You guess the number correctly")
        break
      
if guess == num:
    print("Good job,",name,"you have guess the number in",trial,"guesses")
else:
    print("You guess incorrectly,the number is",num)