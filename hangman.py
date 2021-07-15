import random 
from words import words
import string 

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    lives = 3
    word = get_valid_word(words)
    letters_in_word = set(word)
    alphabet = set(string.ascii_uppercase)
    letters_used = set()

    while len(letters_in_word) > 0 and lives > 0:
        print('You have used these letters: ', ' '.join(letters_used))
        word_list = [letter if letter in letters_used else '-' for letter in word]
        print('Current word is: ', ' '.join(word_list))
        print(f'You have {lives} lives left!')

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - letters_used:
            letters_used.add(user_letter)
            if user_letter in letters_in_word:
                letters_in_word.remove(user_letter)
            else: 
                lives = lives - 1 
                print(f'{user_letter} is not in word')
        elif user_letter in letters_used:
            print('Please choose another character! ')
        else:
            print('Invalid charater, try again!')
    if lives == 0:
        print('Sorry, you lost.... The word was ', word)
    else:
        print('Congratulations, you guessed the word ', word, '!')



hangman()