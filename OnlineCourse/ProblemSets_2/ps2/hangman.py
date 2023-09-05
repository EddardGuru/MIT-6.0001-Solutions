# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    res = ''
    for letter in secret_word:
        if letter in letters_guessed:
            res += letter
        else:
            res += '_ '
    return res


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    english_letters = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in english_letters:
            english_letters.replace(letter, '')
    return english_letters


def get_unique_char(word):
    english_letters = string.ascii_letters
    count = 0

    for letter in word:
        if (letter in english_letters):
            english_letters = english_letters.replace(letter, '')
            count += 1
    return count


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_num = 6
    warnings_num = 3
    secret_word_length = len(secret_word)
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print(
        f"I am thinking of a word that is {secret_word_length} letters long.")
    print(f"You have {warnings_num} warnings left.")
    print("-------------------------------")
    while not is_word_guessed(secret_word, letters_guessed) and guesses_num > 0:
        print(f"You have {guesses_num} guesses left.")
        print(f"Avaliable letters: {get_available_letters(letters_guessed)}\n")
        guess = (input("Please guess a letter: ")).lower()
        cond = guess in letters_guessed
        if not guess.isalpha() or cond:
            internal_guessed_word = get_guessed_word(
                secret_word, letters_guessed)
            if warnings_num <= 0:
                guesses_num -= 1
            warnings_num = 0 if warnings_num <= 0 else warnings_num - 1
            if cond:
                print(
                    f"\nOops! You've already guessed that letter. You now have {warnings_num if warnings_num > 0 else 'You have no warnings left'} warnings: " + internal_guessed_word)
                print("-------------------------------")
            else:
                print(
                    f"\nOops! That is not a valid letter. You have {warnings_num if warnings_num > 0 else 'You have no warnings left'} Warnings left: " + internal_guessed_word)
                print("-------------------------------")
            continue
        letters_guessed.append(guess)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if guess in secret_word:
            guesses_num += 1
            print("\nGood guess: " + guessed_word)
        elif guess in ['a', 'e', 'i', 'o', 'u']:
            guesses_num -= 1
            print("\nOops! That letter is not in my word: ", guessed_word)
        else:
            print("\nOops! That letter is not in my word: ", guessed_word)
        guesses_num -= 1
        print("-------------------------------")
    score = guesses_num * get_unique_char(secret_word)

    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for index in range(len(other_word)):
        letter = my_word[index]
        if letter == '_':
            continue
        if letter != other_word[index]:
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.

    '''
    cond = True
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=" ")
            cond = False
    if cond:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_num = 6
    warnings_num = 3
    secret_word_length = len(secret_word)
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print(
        f"I am thinking of a word that is {secret_word_length} letters long.")
    print(f"You have {warnings_num} warnings left.")
    print("-------------------------------")
    while not is_word_guessed(secret_word, letters_guessed) and guesses_num > 0:
        print(f"You have {guesses_num} guesses left.")
        print(f"Avaliable letters: {get_available_letters(letters_guessed)}\n")
        guess = (input("Please guess a letter: ")).lower()
        cond = guess in letters_guessed
        if not guess.isalpha() or cond:
            internal_guessed_word = get_guessed_word(
                secret_word, letters_guessed)
            if guess == '*':
                show_possible_matches(internal_guessed_word)
                print("-------------------------------")
                continue
            if warnings_num <= 0:
                guesses_num -= 1
            warnings_num = 0 if warnings_num <= 0 else warnings_num - 1
            if cond:
                print(
                    f"\nOops! You've already guessed that letter. You now have {warnings_num if warnings_num > 0 else 'You have no warnings left'} warnings: " + internal_guessed_word)
                print("-------------------------------")
            else:
                print(
                    f"\nOops! That is not a valid letter. You have {warnings_num if warnings_num > 0 else 'You have no warnings left'} Warnings left: " + internal_guessed_word)
                print("-------------------------------")
            continue
        letters_guessed.append(guess)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if guess in secret_word:
            guesses_num += 1
            print("\nGood guess: " + guessed_word)
        elif guess in ['a', 'e', 'i', 'o', 'u']:
            guesses_num -= 1
            print("\nOops! That letter is not in my word: ", guessed_word)
        else:
            print("\nOops! That letter is not in my word: ", guessed_word)
        guesses_num -= 1
        print("-------------------------------")
    score = guesses_num * get_unique_char(secret_word)

    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
