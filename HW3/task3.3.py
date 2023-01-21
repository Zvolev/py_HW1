""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк. 

in
88
out
1011000

in
11
out
1011 """

import os


def clear():
    return os.system('cls')


def decimal_to_binary(num):
    num_bin = []
    while num > 0:
        num_bin.append(int(num % 2))
        num = int(num / 2)
    num_bin.reverse()
    return "".join(map(str, num_bin))


clear()
print(decimal_to_binary(int(input('введите число в десятичном формате => '))))
