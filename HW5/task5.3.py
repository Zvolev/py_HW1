# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 

import os
from random import choice, randint
import time


def start_game():
    print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.')
    time.sleep(1)
    print('Первый ход определяется жеребьёвкой.')
    time.sleep(1)
    print('За один ход можно забрать не более чем 28 конфет.')
    time.sleep(1)
    print('Все конфеты оппонента достаются сделавшему последний ход.')
    time.sleep(1)
    print('Усек правила? Тогда понеслась жара...\n')
    time.sleep(1)
    print("Для начала давай определим кто пойдет первым: введи 0 - если выбираешь ОРЁЛ, 1 - если РЕШКА")
    mychoice = int(input('Удачи => '))
    chance = choice([0, 1])
    print('И кто же пойдет первым...')
    time.sleep(5)
    print("Выпала РЕШКА") if chance else print("Выпал ОРЁЛ")
    if mychoice == chance:
        print("Ходи первым\n")
        return True
    else:
        print("Ты ходишь вторым - зато не теряешь аппонента из вида\n")
        return False


def player_turn():
    print("Сколько возьмешь конфет?")
    turn = 50
    while turn > 28:
        turn = int(input('Только не более 28 =>'))
    print(f'Осталось {candies - turn} конфет\n')
    time.sleep(2)
    return turn


def ai_turn():
    turn = 2023
    while turn > candies:
        if candies <= 28:
            turn = candies
        else:
            turn = candies % 29 if candies % 29 != 0 else randint(1, 28)
    print("ПуКан взял", turn, "конфет")
    print(f'Осталось {candies - turn} конфет\n')
    time.sleep(2)
    return turn


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    if start_game():
        player_first = True
    else:
        player_first = False
    global candies
    candies = 221
    win = ""
    while candies > 1:
        if player_first:
            candies -= player_turn()
            if candies == 0:
                win = "Ты"
                break
            candies -= ai_turn()
            if candies == 0:
                win = "ПуКан"
                break
        else:
            candies -= ai_turn()
            if candies == 0:
                win = "ПуКан"
                break
            candies -= player_turn()
            if candies == 0:
                win = "Ты"
                break
    print("Выиграл", win)


if __name__ == "__main__":
    main()
