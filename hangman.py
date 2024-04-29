import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "science", "coding"]
    random_word = random.choice(words)
    return random_word

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    MAX_ATTEMPTS = 6
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts_left > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("Incorrect guess!")
            attempts_left -= 1
        else:
            print("Correct guess!")

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

    if "_" in display_word(word_to_guess, guessed_letters):
        print("\nOut of attempts! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
