# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def get_num(mass):
    while type:
        get_num = input('{0}=> '.format(mass))
        try:
            get_temp_num = float(get_num)
        except ValueError:
            print('" ' + get_num + ' "' + ' - не является числом')
        else:                                   
            break
    return float(get_num)

x1 = get_num('введите "x" первой точки ')
y1 = get_num('введите "y" первой точки ')
x2 = get_num('введите "x" второй точки ')
y2 = get_num('введите "y" второй точки ')
dist = '{:.2f}'.format(((x2-x1)**2 + (y2-y1)**2)**0.5)
print('расстояние между точками ({0},{1}) и ({2}, {3}) равно {4}'.format(x1, y1, x2, y2, dist))
