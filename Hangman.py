import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # used while what the user has guessed

    lives = 10

# Getting User Input
    while len(word_letters) > 0 and lives > 0:
        #letter used 
        #.join help to convert list into string with the seperate value inside '__'
        print("You have ",lives," Lives." "You have used these letters: ",' '.join(used_letters))
        #what current word is (ie -- W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        user_letters =input("Guess a Letter: ").upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)

            else:
                lives = lives - 1
                print("Letter is not in the word.")

        elif user_letters in used_letters:
            print("You already Used that character.Please try Again...")
        else:
            print("Invalid Character.Please Try Again...")
    if lives == 0:
        print("You Died!!! Sorry. The word is ",word)
    else:
        print("Hurryy!!! You guessed the word",word, "correctly")



hangman()



    