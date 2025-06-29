# Problem Set 2, hangman.py
# Name: Krishtina Maharjan
# Collaborators: None
# Time spent:

import string, random

def choose_word():
    with open('words.txt', 'r') as f:
        wordlist = f.read().split()
        if not wordlist:
            print("Error: 'words.txt' is empty."); exit()
        return random.choice(wordlist)

def is_word_guessed(secret, guesses):
    for c in secret:
        if c not in guesses: return False
    return True

def get_guessed_word(secret, guesses):
    return ''.join(c if c in guesses else '_ ' for c in secret)

def get_available_letters(guesses):
    return ''.join(c for c in string.ascii_lowercase if c not in guesses)

def check_warnings(warnings, guess, duplicates, display):
    warnings -= 1
    if not guess.isalpha():
        print(f'Oops! That is not a valid letter. You have {warnings} warnings left: {display}')
    elif guess in duplicates:
        print(f'Oops! You\'ve already guessed that letter. You have {warnings} warnings left: {display}')
    print('-----------------')
    return warnings

def check_guesses(guesses, guess, duplicates, display):
    guesses -= 1
    if not guess.isalpha():
        print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {display}")
    elif guess in duplicates:
        print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {display}")
    else:
        print(f"Oops! That letter is not in my word: {display}")
    print('-----------------')
    return guesses

def hangman(secret):
    guesses, warnings, display = 6, 3, '_ ' * len(secret)
    guessed, duplicates = [], []
    unique = ''.join(set(secret))

    print('Welcome to the game Hangman!')
    print(f"I'm thinking of a word that is {len(secret)} letters long.")
    print(f'You have {warnings} warnings left.\n-----------------')

    while True:
        print(f'You have {guesses} guesses left.')
        print('Available letters: "' + get_available_letters(guessed) + '"')
        guess = input('Please guess a letter: ').lower()

        if not guess.isalpha():
            if warnings > 0:
                warnings = check_warnings(warnings, guess, duplicates, display)
            elif guesses > 1:
                guesses = check_guesses(guesses, guess, duplicates, display)
            else:
                print(f'Sorry, you ran out of guesses. The word was {secret}.')
                break
        else:
            if guess not in guessed:
                guessed.append(guess)
            if is_word_guessed(secret, guessed):
                print('Good guess:', display)
                print('-----------------')
                print('Congratulations, you won!')
                print(f'Your total score is: {guesses * len(unique)}')
                break
            elif guess in duplicates:
                if warnings > 0:
                    warnings = check_warnings(warnings, guess, duplicates, display)
                elif guesses > 1:
                    guesses = check_guesses(guesses, guess, duplicates, display)
            elif guess in secret:
                display = get_guessed_word(secret, guessed)
                print('Good guess:', display)
                print('-----------------')
            else:
                if guess in 'aeiou' and guesses > 1:
                    guesses -= 1
                if guesses > 1:
                    guesses = check_guesses(guesses, guess, duplicates, display)
                else:
                    print(f'Oops! That letter is not in my word: {display}')
                    print('-----------------')
                    print(f'Sorry, you ran out of guesses. The word was {secret}.')
                    break
        duplicates.append(guess)
        print(duplicates)

secret_word = choose_word()
hangman(secret_word)
