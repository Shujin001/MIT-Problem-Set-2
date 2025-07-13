# Problem-Set-2, hangman.py
# Name: Chirag Sharma
# Collaborators: None
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    displayed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            displayed_word += letter
        else:
            displayed_word += "*"
    return displayed_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    available = [letter for letter in all_letters if letter not in letters_guessed]
    return "".join(available)



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_left = 10
    letters_guessed = []
    vowels = "aeiou"

    print("Hey there! Welcome to Hangman!")
    print(f"I'm thinking of a word that's {len(secret_word)} letters long.")
    print(f"You get 10 guesses to figure it out. Good luck!\n")

    while guesses_left > 0:
        print("--------------------------------------------------")
        print(f"You have {guesses_left} guess{'es' if guesses_left != 1 else ''} left.")
        print("Letters you haven't guessed yet:", get_available_letters(letters_guessed))
        current_progress = get_word_progress(secret_word, letters_guessed)
        print("So far, the word looks like this:", current_progress)

        guess = input("Guess a letter (or type '!' for a hint): ").lower()

        # Handle help feature if enabled
        if with_help and guess == "!":
            if guesses_left < 3:
                print("Hmm, you need at least 3 guesses left to use a hint. Keep trying!")
            else:
                missing_letters = [l for l in secret_word if l not in letters_guessed]
                if missing_letters:
                    hint_letter = random.choice(missing_letters)
                    letters_guessed.append(hint_letter)
                    guesses_left -= 3
                    print(f"Alright, here's a hint: The letter '{hint_letter}' is in the word!")
                else:
                    print("You're so close! No letters left to reveal.")
            continue

        # Validate input
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Oops! That's not a valid letter. Please enter just one alphabet letter.")
            continue

        if guess in letters_guessed:
            print("You've already guessed that letter. Try a different one!")
            continue

        # Add guess to list
        letters_guessed.append(guess)

        if guess in secret_word:
            print("Nice! That letter is in the word.")
        else:
            print("Sorry, that letter isn't in the word.")
            # Deduct guesses (2 if vowel, else 1)
            if guess in vowels:
                guesses_left -= 2
                print("Since it's a vowel, you lose 2 guesses.")
            else:
                guesses_left -= 1

        # Show progress after guess
        print("Here's how the word looks now:", get_word_progress(secret_word, letters_guessed))

        # Check if player won
        if has_player_won(secret_word, letters_guessed):
            print("\n🎉 Congratulations! You've guessed the word! You win!")
            break

        # Check if guesses are exhausted
        if guesses_left <= 0:
            print("\n😢 Oops! You're out of guesses. The word was:", secret_word)
            print("Better luck next time!")

    print("Thanks for playing Hangman. See you around!")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
     secret_word = choose_word(wordlist)
     with_help = True  # or False if you want to test without the '!' feature
     hangman(secret_word, with_help)

