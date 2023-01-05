""" # 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


def check():
    enter_list = input("Введите числа через пробел ").split()
    right_list = []
    for i in range(len(enter_list)):
        enter_list[i] = enter_list[i].strip("!,;")
    if enter_list[i].isdigit:
        right_list.append(enter_list[i])
    print(right_list)
    return right_list


def max_min_finder(any_list):
    if any_list:
        return max(any_list, key=int), min(any_list, key=int)
    return []


print(*max_min_finder(check())) """


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.


from math import sqrt


def find_r(a, b, c):
    D = b**2 - 4*a*c
    with open("Diskr.txt", "a", encoding="utf-8") as my_f:
        my_f.write(F"{a}x² + {b}x + {c} = 0\n")
        if D > 0:
            x1 = (-b - sqrt(D)) / (2*a)
            x2 = (-b + sqrt(D)) / (2*a)
            my_f.write(f"{x1, x2}\n")
        elif D == 0:
            x = -b / (2*a)
            my_f.write(f"{x}\n")
        else:
            my_f.write("нет корней\n")


find_r(3, 8, 5)

# 3. На вход программе подается число n.
# Программа печатает численный треугольник.
# Используем вложенные циклы.

""" iteration = int(input("Введите число -> "))
for i in range(1, iteration+1):
    for k in range(i):
        print(i, end='')
    print()
 """

""" Простые делители числа
https://autogear.ru/article/371/831/chislo-prostyih-deliteley-chisla-skolko-deliteley-imeet-prostoe-chislo/
https://calc.ws/simple-num-mnoj.php?num=650 """