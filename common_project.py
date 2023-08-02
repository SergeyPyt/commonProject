from random import choice, sample

from PIL import Image

from constants import LETTERS


def get_guess_word(word_list):
    word = choice(word_list)
    return word


def get_photos(picture_dictionary, word):
    rand_list = []
    for w in picture_dictionary:
        if word in picture_dictionary[w]:
            rand_list.append(w)

    rand_elements = sample(rand_list, 2)
    for elements in rand_elements:
        img = Image.open(elements)
        img.show()
        img.close()


def guess(word):
    res = ['*'] * len(word)
    count = 0
    print(f'''Добро пожаловать в игру угадай слово
    я загадал слово "{"".join(res)}" из {len(word)} букв, вам надо угадать его.''')
    while True:
        char = input('Введите букву или слово целиком: ').lower()
        if char == word:
            break
        if char not in LETTERS:
            print('Нужно ввести букву от a до z')
            continue
        elif char in word:
            for i, v in enumerate(word):
                if v == char:
                    res[i] = char
            print(f'Поздравляю эта буква есть в загаданном слове "{"".join(res)}"')
            count += 1
        else:
            print('В этом слове нет такой буквы')
        if '*' not in res:
            break

    if not count:
        print("Вы угадали слово сразу")
    else:
        print(f'Вы угадали слово количество попыток: {count}')

"""рефактор while
фотки в папку статик
закинуть на гит(сделать публичным)
создат что бы как экзешник запускалось не.py а .exe
добавить категории и добавить фотки(можно нюдс и гачи)
смотреть граф интерфейс как оформить!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
бтблиотелки пайГЕЙм, кьютидизайнер"""
