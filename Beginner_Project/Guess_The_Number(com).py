#BEGINNER PROJECT
#2 Guess The Number (computer)

# Guess the number that which the number is secretly assigned by the computer
# before, try to access the document regarding random syntax at python ofc website

import random

print(" Welcome to Guess the Number Game.")
print(" The computer will set the number and your task is to guess the number")
print(" LETSS GOO !!!\n")

def guess(x, y):
    random_num = random.randint(x, y)
    guess = 0
    while guess != random_num:
        guess = int(input("Guess the number: "))
        if guess > random_num:
            print("Sorry your number is too high!")
        elif guess < random_num:
            print("Sorry your number is too low!")
    print(f"Congratulations, you have guess number {random_num} Correctly!!! ")

small_num = int(input(" Input the small range number: "))
large_num = int(input(" Input the big range number: "))
guess(small_num,large_num)
