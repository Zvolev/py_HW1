""" Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных/четных позициях(не индексах).
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

from random import randint, sample
import os
clear = lambda: os.system('cls')
clear()

def create_rand_list(len, start=0, stop=len):
    #rand_list = []
    #for _ in range(len):
    #   rand_list.append(randint(start, stop))
    rand_list = sample((range(start, stop)), len)  
    return rand_list
    
    
my_rand_list = create_rand_list(int(input('введите длину списка => ')), 
                    int(input('введите начало диапазона => ')), 
                    int(input('введите конец диапазона => ')))
print(my_rand_list)
sum_element_list =0

""" for i in range(0, len(my_rand_list), 2):
    sum_element_list += my_rand_list[i]
print(f'сумма нечетных элементов списка: {sum_element_list}') """

for i in range(1, len(my_rand_list), 2):
    sum_element_list += my_rand_list[i]
print(f'сумма четных элементов списка: {sum_element_list}')
