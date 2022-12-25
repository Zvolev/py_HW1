""" Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
in
5
out
[5.16, 8.62, 6.57, 7.92, 9.22]
Min: 0.16, Max: 0.92. Difference: 0.76

in
3
out
[9.26, 8.5, 1.14]
Min: 0.14, Max: 0.5. Difference: 0.36 """

from math import trunc
from random import uniform
import os


def clear():
    return os.system('cls')


def create_rand_list_2floatsize(length, start=0, stop=1, size_round=2):
    rand_list = []
    for i in range(length):
        rand_list.append(round(uniform(start, stop), size_round))
    print(f'Начальный список  => {rand_list}')
    for i in range(length):
        rand_list[i] = (
            round((rand_list[i] - trunc(rand_list[i])), size_round))
    print(f'Его дробная часть => {rand_list}')
    return rand_list


def min_max_difference(work_list, size_round):
    min_list = min(work_list)
    max_list = max(work_list)
    diff = round((max(work_list)-min(work_list)), size_round)
    print(f'Min: {min_list}, Max: {max_list}. Difference: {diff}')


clear()
size_round = int(input('сколько точек используем после запятой? => '))
my_list = create_rand_list_2floatsize(int(input('введите длину списка => ')),
                                      int(input('введите начало диапазона => ')),
                                      int(input('введите конец диапазона => ')), size_round)
min_max_difference(my_list, size_round)
print()
