import random
import string

words = ['hello', 'world']

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #getting user input
    while len(word_letters) > 0:
        print("you have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current word is: ", ' '.join(word_list))

        user_letter = input("\nguess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("you have already guessed that word")
        else:
            print("Invalid character")
    print("You Guessed the Word: ",word, '!!')

hangman()
