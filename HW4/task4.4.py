""" Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
записать в файл полученный многочлен не менее 3-х раз.
in
9
5
3
out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
4*x^2 - 4 = 0

in
0
-1
4
out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
4*x^2 - 4 = 0
2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0 """



""" from random import randint, sample
def create_polinom(degree: int):
    polinom_list = []
    coefficient = sample(range(-10, 10), 15)
    coef_i = 0
    with open("poly.txt", "a", encoding="utf-8") as my_f:
        while degree >= 0:
            if degree > 1:
                if coefficient[coef_i] > 0:
                    my_f.write(f'+ {coefficient[coef_i]}*x^{degree} ')
                else:
                    my_f.write(f'- {abs(coefficient[coef_i])}*x^{degree} ')
            elif degree == 1:
                if coefficient[coef_i] > 0:
                    my_f.write(f'+ {coefficient[coef_i]}*x ')
                else:
                    my_f.write(f'- {abs(coefficient[coef_i])}*x ')
            elif degree == 0:
                if coefficient[coef_i] > 0:
                    my_f.write(f'+ {coefficient[coef_i]} ')
                else:
                    my_f.write(f'- {abs(coefficient[coef_i])} ')
            degree -= 1
            coef_i += 1
        my_f.write('\n')


create_polinom(6) """

from random import randint, sample
def create_polinom(degree: int):
    polinom_list = []
    coefficient = sample(range(-10, 10), 15)
    coef_i = 0
    with open("poly_2.txt", "a", encoding="utf-8") as my_f:
        while degree >= 0:
            if degree > 1:
                if coefficient[coef_i] > 0:
                    my_f.write(f'+ {coefficient[coef_i]}*x^{degree} ')
                else:
                    my_f.write(f'- {abs(coefficient[coef_i])}*x^{degree} ')
            elif degree == 1:
                if coefficient[coef_i] > 0:
                    my_f.write(f'+ {coefficient[coef_i]}*x ')
                else:
                    my_f.write(f'- {abs(coefficient[coef_i])}*x ')
            elif degree == 0:
                if coefficient[coef_i] > 0:
                    my_f.write(f'+ {coefficient[coef_i]} ')
                else:
                    my_f.write(f'- {abs(coefficient[coef_i])} ')
            degree -= 1
            coef_i += 1
        my_f.write('\n')


create_polinom(2)