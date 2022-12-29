""" Задайте последовательность чисел. Напишите программу, которая выведет 
список неповторяющихся элементов исходной последовательности в том же порядке.

in
7
out
[4, 5, 3, 3, 4, 1, 2]
[5, 1, 2]

in
-1
out
Negative value of the number of numbers!
[]

in
10
out
[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
[6, 2, 3, 0, 9] """

from random import randint
import os
def clear(): return os.system('cls')


clear()


def create_rand_list(len: int):
    rand_list = []
    for _ in range(len):
        rand_list.append(randint(0, len))
    return rand_list


def non_repeating_elements(lst: list):
    new_lst = []
    i = 0
    while i < len(lst):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
        i += 1
    return new_lst


my_rnd_list = create_rand_list(int(input('введите длину массива ')))
print(my_rnd_list)
print(non_repeating_elements(my_rnd_list))
