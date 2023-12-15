# У файлі hangman.py
import random


def welcome():
    print("HANGMAN\nWelcome to the Hangman game!")


def show_hint(word, correct_letters):
    # Показати слово з розкритими літерами та дефісами
    display_word = ''.join([letter if letter in correct_letters else '-' for letter in word])
    print(display_word)


def play_hangman():
    # Створити список слів
    words = ['python', 'java', 'javascript', 'php']

    # Випадково вибрати слово зі списку
    chosen_word = random.choice(words)

    # Літери, які вже вгадані
    correct_letters = set()

    # Кількість помилок, що залишилися
    attempts_left = 8

    while attempts_left > 0:
        # Показати кількість спроб, що залишилися
        print(f"Attempts left: {attempts_left}")

        # Показати слово з розкритими літерами та дефісами
        show_hint(chosen_word, correct_letters)

        # Запитати гравця вгадати літеру
        guess = input("Input a letter: > ").lower()

        # Перевірити введену літеру
        if len(guess) != 1:
            print("You should input a single letter")
        elif not guess.isalpha() or not guess.isascii():
            print("Please enter a lowercase English letter")
        elif guess in correct_letters:
            print("You've already guessed this letter")
        elif guess in chosen_word:
            print("No improvements")
            correct_letters.add(guess)
        else:
            print("That letter doesn't appear in the word")
            attempts_left -= 1

        # Перевірити, чи всі літери вгадані
        if set(chosen_word) == correct_letters:
            show_hint(chosen_word, correct_letters)
            print("Congratulations! You guessed the word!")
            print("You survived!")
            break

    # Гравець використав всі спроби
    else:
        show_hint(chosen_word, correct_letters)
        print("Thanks for playing!\nYou lost!")


# Головна функція для вибору гравцем гри або виходу
def main():
    while True:
        choice = input("Type 'play' to play the game, 'exit' to quit: > ").lower()
        if choice == 'play':
            play_hangman()
        elif choice == 'exit':
            break
        else:
            print("Invalid choice. Please type 'play' or 'exit'.")


if __name__ == "__main__":
    # Викликати вітання та головну функцію гри
    welcome()
    main()
