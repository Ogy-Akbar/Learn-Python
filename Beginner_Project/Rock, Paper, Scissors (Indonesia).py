#BEGINNER PROJECT
#4 Rock, Paper, Scissors

# Play Rock, Paper, & Scissors with Computer
# This Version will be using the Indonesian Version


import random

def instruction():
    print("Welcome To The Rock, Paper, and Scissors\n")
    print("But, this game will be using the Indonesia Version Which using:")
    print(" 1. Gajah (Elephant) => G\n"
      " 2. Manusia (Human) => M\n"
      " 3. Semut (Ant) ")
    print("\nThe Rule is Pretty simple: \n"
      " * Gajah wins against Human or G > H\n"
      " * Manusia wins against Semut or H > S\n"
      " * Semut wins against Gajah or S > H")
    print("\n if you like to quit, just press 'Q' ")
    print("\nOkey.. If You are ready, Let's Get Started!!!")
    
def play():
    choices = {'g': 'Gajah', 'm' : 'Manusia', 's': 'Semut'}
    
    while True:
        user = input("What would You pick, 'G' or 'M', 'S' or 'Q'?").lower()
        if user == 'q':
            return None
        elif user in choices:
            break
        else:
            print("X invalid choice, please pick again!")
    
    com = random.choice(list(choices.keys()))
    
    print(f"You Chose: {choices[user]} | Opponent Chose: {choices[com]}")
    
    if user == com:
        return "Its a Tie"
    
    if is_win(user, com):
        return "You Won"
    
    return "You Lost"
    
    
def is_win(player, opponent):
 # return true if player wins
 # G > H, H > S, or S > H
 if (player == 'g' and opponent == 'm') or (player == 'm' and opponent == 's') or (player == 's' and opponent == 'g'):
     return True

def game():
    instruction()
    while True:
        result = play()
        if result is None:
            print("Thank you for Playing!")
            break
        print(result + "\n")
    
game()
