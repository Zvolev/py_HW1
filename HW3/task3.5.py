""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Негафибоначчи

in
8
out
-21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

in
5
out
5 -3 2 -1 1 0 1 1 2 3 5 """


import os


def clear():
    return os.system('cls')


def negafibonachi(num):
    fib_list = [0]
    if num >= 1:
        fib_list.append(1)
        fib_list.insert(0, 1)
        if num > 1:
            for i in range(num-1):
                a = fib_list[-1] + fib_list[-2]
                fib_list.append(a)
                fib_list.insert(0, ((-1)**(i+1))*a)
    print(" ".join(map(str, fib_list)))

clear()
num = int(input('Задайте число => '))
print('Cписок чисел Фибоначчи/Негафибоначчи: ', end='')
negafibonachi(num)