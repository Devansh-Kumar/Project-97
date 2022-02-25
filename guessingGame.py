import random
numbers = ['1','2','3','4','5','6','7','8','9']

print("Number Guessing Game")
print("Guess a Number (between 1 to 9):")

numbers = int(input("Enter your Guess:- "))    
if (numbers < 8):
    print("Try Again")
if (numbers == 9):
    print("Congratulations, You Have WON!")