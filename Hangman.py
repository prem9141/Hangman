import random
import hangman_art as ha
from hangman_words import word_list

lives = 6

selected_word = random.choice(word_list)
word_length = len(selected_word)
display_word = ["_"] * word_length

found_word = 0
print(ha.logo)
print(f"{' '.join(display_word)}")

while found_word != word_length and lives != 0:
    letter = input("Guess a letter: ").lower()
    letter_found = False
    if letter not in display_word:
        for index, word in enumerate(selected_word):
            if word == letter:
                display_word[index] = letter
                found_word += 1
                letter_found = True
    else:
        print(f"You've already guessed {letter}")
        letter_found = True

    if not letter_found:
        lives -= 1
        print(f"You guessed {letter}, that's not in the word. You lose a life")
        print(ha.stages[lives])
    else:
        print(f"{' '.join(display_word)}")


if lives == 0:
    print("Sorry you lost")
else:
    print("You won!!!")
