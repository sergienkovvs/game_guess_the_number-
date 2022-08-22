import random

def get_user_number():
    user_number = input("Введите число: ")
    return user_number


def generete_random_number():
    random_number = random.randint(0,100)
    return random_number


def check_user_number(user_number:str):
    user_number = int(user_number)
    if user_number < 0:
        print("Должно быть ЧИСЛО, больше 0 и меньше 100")
        raise ValueError
    elif user_number > 100:
        print("Должно быть ЧИСЛО, больше 0 и меньше 100")
        raise ValueError
    return user_number


def win_game(user_number, random_number):
    if user_number == random_number:
        exit()


def compeire_numbers1(user_number, random_number):
    if user_number < random_number:
        print("Загаданное число меньше")
        raise ValueError


def compeire_numbers2(user_number, random_number):
    if user_number > random_number:
        print("Загаданное число больше")
        raise ValueError


def exit_game(user_data):
    if user_data == "exit":
        exit()

random_number = generete_random_number()

for counter in range(0,5):
    try:
        user_string = get_user_number()
        exit_game(user_string)
        user_number = check_user_number(user_string)
        win_game(random_number,user_number)
        compeire_numbers1(random_number,user_number)
        compeire_numbers2(random_number,user_number)
    except ValueError:
        pass