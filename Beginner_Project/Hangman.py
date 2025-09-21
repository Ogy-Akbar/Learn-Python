import random
from Random_Words import rand_words # import rand_words list from Random_words.py
import string

def get_valid_words(words):
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(rand_words) # get random words from the ran_words list
    word_letters = set(word) # Create Set for the random words
    alphabet = set(string.ascii_uppercase) # Set of alphabet
    used_letters = set() # Containing the already used letters

    while len(word_letters) > 0: # making sure that there is a letter in the words_letters set
        # User needs to know what letters have been used
        # " ", join["a", "b", "cd"] --> "a b cd"
        print("You have used these letters: ", " ".join(used_letters))

        # Tell the user what are the current characters
        word_lists = [letter if letter in used_letters else "_" for letter in word]
        print("Current words: ", " ".join(word_lists))

        # getting input from the user
        user_letters = input("Guess a letter: ").upper()

        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)

        elif user_letters in used_letters:
            print("You have already used the character, please try again!")

        else:
            print("Invalid Character, please try again")

    print(f"Congratulations, You have guessed the word, {word} !!")

hangman()

