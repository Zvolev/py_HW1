# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def get_num(mass):
    while type:
        get_num = input('{0}=> '.format(mass))
        try:
            get_temp_num = int(get_num)
        except ValueError:
            print('" ' + get_num + ' "' + ' - не является числом')
        else:                                   
            break
    return get_num

def num_quarter(quarter):
    if quarter == 1:
        print('диапазон возможных координат точек (x > 0, y > 0)')
    elif quarter == 2:
        print('диапазон возможных координат точек (x < 0, y > 0)')    
    elif quarter == 3:
        print('диапазон возможных координат точек (x < 0, y < 0)')      
    elif quarter == 4:
        print('диапазон возможных координат точек (x > 0, y < 0)')
    else:
        print('введены некорректные данные')

quarter = int(get_num('Введите номер четверти координатной плоскости '))
num_quarter(quarter)
