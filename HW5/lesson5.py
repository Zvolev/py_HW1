""" # 1. Создайте список из N натуральных чисел(0 до N),
# упорядоченных по возрастанию. Среди чисел не хватает
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.
from random import choice

def any_list(num):
    a_list = list(range(num+1))
    a_list.remove(choice(a_list))
    return a_list

def find(n_list):
    for i in range(1, len(n_list)):
        if n_list[i] -1 != n_list[i-1]:
            return n_list[i] -1
    return -1


data = any_list(int(input("Введите число: ")))
print(data)
number = find(data)
print(number)    """

# 2. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import choices


def any_list(num):
return choices(range(1, num+2), k=num)


def seq(some_list):
temp_list = []
for i in range(len(some_list)):
num_1 = some_list[i]
out_list = [num_1]
for j in range(i+1, len(some_list)):
if some_list[j] > num_1:
num_1 = some_list[j]
out_list.append(num_1)
if len(out_list) > 1:
temp_list.append(out_list)
return temp_list


a = any_list(10)
print(a)
print(seq(a))





""" Мария Андреева: https://www.youtube.com/watch?v=q_N2Y6-O1xw&ab_channel=dinsky
Соломкин Александр: благодарю)
Мария Андреева: from os import path
Мария Андреева: if path.exists(text):
Мария Андреева: itertools import groupby """