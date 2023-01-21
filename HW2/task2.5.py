""" Реализуйте алгоритм перемешивания списка.
Без функции shuffle из модуля random.
10
-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8] """
import random

num = int(input('введите число -> '))
my_list = []
for i in range(num):
    my_list.append(i)
    i+=1
print(my_list)

def mix_list(my_list, num):
    new_list = []
    for i in range(num):
        j = random.randrange(num)
        n = my_list.pop(j)
        new_list.append(n)
        i+=1
        num-=1
    return new_list

new_mix_list = mix_list(my_list, num)

print(new_mix_list)