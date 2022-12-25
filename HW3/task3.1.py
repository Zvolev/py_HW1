""" Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
in
5

out
[10, 2, 3, 8, 9]
22

in
4

out
[4, 2, 4, 9]
8 """

from random import randint
import os
clear = lambda: os.system('cls')
clear()

def create_rand_list(len, start=0, stop=len):
    rand_list = []
    for _ in range(len):
        rand_list.append(randint(start, stop))
    return rand_list
    
    
my_rand_list = create_rand_list(int(input('введите длину списка => ')), 
                    int(input('введите начало диапазона => ')), 
                    int(input('введите конец диапазона => ')))
print(my_rand_list)
sum_element_list = sum(my_rand_list)
print(f'сумма элементов списка: {sum_element_list}')