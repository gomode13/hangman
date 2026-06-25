import os
import random
import sys
import time
import re

STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words(file_path):
    try:
        with open (file_path, 'r', encoding='utf-8') as f:
            return [i for i in f.read().split() if 5 <= len(i) <= 10]
    except FileNotFoundError:
        print('Файл не найден. Игра невозможна.')

def display_game_state(stages, errors, hidden_word, used_letters):
    clear_screen()
    print(stages[errors])
    print(f"Количество ошибок: {errors}")
    print('Слово: '+ ' '.join(hidden_word))
    print('Введенные буквы: ' + ' '.join(used_letters))

def get_valid_letter(used_letters):
    while True:
        char = input('Введите букву: ').lower().strip()
        if len(char) != 1:
            print('Нужно ввести ровно ОДНУ букву.')
        elif not char.isalpha():
            print('Это не буква! Попробуйте еще раз.')
        elif not bool(re.match(r'[а-яё]', char, re.IGNORECASE)):
            print('Введите букву из русского алфавита!')
        elif char in used_letters:
            print('Вы уже вводили эту букву.')
        else:
            return char

def play_game(word):
    errors = 0
    used_letters = []
    hidden_word = list('_' * len(word))
    while True:
        display_game_state(STAGES, errors, hidden_word, used_letters)

        c = get_valid_letter(used_letters)
        used_letters.append(c)

        if c in word:
            for index, letter in enumerate(word):
                if c == letter:
                    hidden_word[index] = letter

        else:
            print('В слове нет такой буквы...\n')
            errors += 1
            time.sleep(1)

        if ''.join(hidden_word) == word:
            clear_screen()
            print('Вы победили!!!\n***')
            print(f"Загаданное слово: {word}\n")
            break

        if errors == len(STAGES) - 1:
            clear_screen()
            print(STAGES[errors])
            print('Вы проиграли\n***')
            print(f"Загаданное слово: {word}\n")
            break



if __name__ == '__main__':
    words = load_words('russian-mnemonic-words.txt')
    if not words:
        print('Нет доступных слов. Игра невозможна.')
        sys.exit()

    while True:
        choice = input('Игра "Виселица":\n1. Начать новую игру.\n2. Выйти из игры.\n').strip()
        if choice == '1':
            word = random.choice(words)
            play_game(word)
        elif choice == '2':
            break
        else:
            clear_screen()
            print('Введите 1 - Начать новую игру или 2 - Выйти из игры.')


