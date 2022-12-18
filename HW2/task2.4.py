""" Напишите программу, которая принимает на вход 2 числа.
Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
Найдите произведение элементов на указанных позициях(не индексах).
Enter the value of N: 5
Position one: 1
Position two: 2
-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
-> 20

Enter the value of N: 4
Position one: 20
Position two: 22
-> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
-> There are no values for these indexes! """

num = int(input('Enter the value of N: '))
my_list = []
for i in range(-num, num+1):
    my_list.append(i)
    i+=1
print('-> ', my_list)

pos1 = int(input('Position one: '))
pos2 = int(input('Position two: '))

if pos1 >= 1 and pos2 <= num*2+1:
    deriv = my_list[pos1-1] * my_list[pos2-1]
    print('-> ', deriv)
else:
    print('-> There are no values for these indexes!')






