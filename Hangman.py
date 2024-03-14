import random

filename = 'words.txt'

# function to get the random word from the file
def get_random_word(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
        random_word = random.choice(words).strip().lower()

    return random_word
# function that handle the steps that the game is moved through
def ingame(word):
    global guessed
    guessed = False  # the condition of guessing the word is false
    dashes_perword = "_" * len(word)
    word_guessed = False # the word not guessed
    letter_guessed = [] # list that contains the letters that gussed by user
    full_word_guess = [] # list that contains the full word that is guessed
    limits = 6
    print("Enjoy")
    print(display_hangman(limits))
    print(dashes_perword)
    print("\n")
    while not word_guessed and limits > 0:
        guess = input("please enter your guess: ").lower()

        # if user's input is a letter
        if len(guess) == 1:
            if guess in letter_guessed:
                print("You already tried" + " " + guess)
            elif guess not in word:
                print(guess, "Is the wrong letter")
                limits -= 1
                letter_guessed.append(guess)
            else:
                print("You got it right!!")
                letter_guessed.append(guess)
                word_as_list = list(dashes_perword)

                for i, letter in enumerate(word):
                    if letter == guess:
                        word_as_list[i] = guess

                dashes_perword = "".join(word_as_list)

                if "_" not in dashes_perword:
                    guessed = True
                    break
        # if user's input is a word
        elif len(guess) == len(word):
            if guess in full_word_guess:
                print("you already tried")
            elif guess != word:
                print(guess, "is the wrong word")
                limits -= 1
                full_word_guess.append(guess)
            else:
                guessed = True
                dashes_word = word
                break
        else:
            print("invalid")
        print(display_hangman(limits))
        print(dashes_perword)
        print("\n")
    if guessed == True:
        print("Nice work")
        print(word)
    else:
        print("oops,you could not guess this word")
        print(word)

# function displays the shape of hangman during the game
def display_hangman(limits):
    stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
                """,
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
                """,
              """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                -
                """,
              """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                -
                """,
              """
                --------
                |      |
                |      O
                |
                |
                |
                -
                """,
              """
                --------
                |      |
                |      
                |
                |
                |
                -
                """
              ]
    return stages[limits]

# main function to start and run the game
def main():
    word = get_random_word(filename)
    ingame(word)
    while input("Again? (Y/N) ").upper() == "Y":
        word = get_random_word(filename)
        ingame(word)
    print("GoodBye")


if __name__ == "__main__":
    main()
