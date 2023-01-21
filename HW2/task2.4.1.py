""" Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число. """


num = int(input('Введите значение N: '))
my_list = []
for i in range(-num, num+1):
    my_list.append(i)
    i+=1
print('-> ', my_list)

pos1 = int(input('Позиция первого элемента: '))
pos2 = int(input('Позиция второго элемента: '))
position = open('file.txt', 'w')
position.write('{}\n'.format(pos1))
position.write('{}\n'.format(pos2))
position.close()

input('Считать данные о позициях из файла и расчитать произведение элементов? => ')
pos_list = []
path = 'file.txt'
position = open(path, 'r')
for line in position:
    pos_list.append(int(line))

if pos_list[0] >= 1 and pos_list[1] <= num*2+1:
    deriv = my_list[pos_list[0]-1] * my_list[pos_list[1]-1]
    print('Произведение элементов = ', deriv)
else:
    print('Нет значений для этих позиций!')