""" Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
(или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

def get_num(mass):
    while type:
        get_num = input('{0}=> '.format(mass))
        try:
            get_temp_num = float(get_num)
        except ValueError:
            print('"' + get_num + '"' + ' - не является числом')
        else:                                   
            break
    return get_num

def coordinate_plane(x, y):  
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            n = 1
        elif x < 0 and y > 0:
            n = 2
        elif x < 0 and y < 0:
            n = 3
        else:
            n = 4
        print('точка с координатами ({0}, {1}) находится в {2} четверти'.format(x, y, n))
    else: print('введены некорректные данные, по условиям задачи x ≠ 0 и y ≠ 0')

print('Введите координаты:')
x = float(get_num('x '))
y = float(get_num('y '))
coordinate_plane(x, y)
