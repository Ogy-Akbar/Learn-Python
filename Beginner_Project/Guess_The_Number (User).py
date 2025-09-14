#BEGINNER PROJECT
#3 Guess The Number (User)

# Different with before, this one user will have a secret number and the computer should guess it
# before, try to access the document regarding random syntax at python ofc website

import random

print(" Welcome to Guess the Number Game.")
print(" This is one is  a bit different\n You will have a secret number and the computer will guess it")
print(" ARE YOU READY???\n LETSS GOO !!!\n")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess_num = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # it could be high since low = high

        guess_num += 1
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay, You computer have guess the number {guess} with {guess_num} guese(s)!!!")

computer_guess(50)
