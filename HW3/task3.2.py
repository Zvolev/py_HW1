""" Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
in
4

out
[2, 5, 8, 10]
[20, 40]

in
5

out
[2, 2, 4, 8, 8]
[16, 16, 4] """

from random import randint
import os
clear = lambda: os.system('cls')
clear()

def create_rand_list(length, start=0, stop=len):
    rand_list = []
    for _ in range(length):
        rand_list.append(randint(start, stop))
    return rand_list

def sum_of_pairs_list(work_list):
    for i in range(int(len(work_list)/2)):
        work_list[i] *= work_list.pop(-1)
    return work_list    
       
my_rand_list = create_rand_list(int(input('введите длину списка => ')), 
                    int(input('введите начало диапазона => ')), 
                    int(input('введите конец диапазона => ')))

print(my_rand_list)
print(sum_of_pairs_list(my_rand_list))