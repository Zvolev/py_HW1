# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов
# 8. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

num_1 = '83*x^2 + 43*x + 57 = 0'.replace(' ', '')
num_1 = num_1[:num_1.find('=')].split('+')

num_2 = '23*x^5 + 25*x^4 + 37*x^3 + 72*x^2 + 41*x + 52 = 0'.replace(' ', '')
num_2 = num_2[:num_2.find('=')].split('+')
num_all = num_1 + num_2

my_dict = {}

for elem in num_all:
    if 'x' not in elem:
        key = 0
    elif '^' not in elem:
        key = 1
    else:
        key = int(elem[elem.find('^') + 1:])

    if key > 0:
        if key in my_dict:
            my_dict[key] += int(elem[:elem.find('*')])
        else:
            my_dict[key] = int(elem[:elem.find('*')])
    else:
        if key in my_dict:
            my_dict[0] += int(elem)
        else:
            my_dict[0] = int(elem)
    print(my_dict)

my_str = ''
for key, value in sorted(my_dict.items(), reverse=True):
    if key == 0:
        my_str += str(value)
    elif key == 1:
        my_str += f'{value}*x + '
    else:
        my_str += f'{value}*x^{key} + '

my_str = my_str + ' = 0'

# # Функция парсинга строки в список, раздляя ее по пробелам и удаляя знаки + и =
# def parse_poly(_string):
#     my_list = list(_string.split())
#     for i in my_list:
#         if "+" in my_list:
#             my_list.remove("+")
#         if "=" in my_list:
#             my_list.remove("=")
#     # удаляем последний элемент (который "= 0")
#     my_list.pop()
#     return my_list
#
#
# # Функция чтения строки из файла
# def readFromFile(_file):
#     data = ""
#     with open(_file) as rfile:
#         data = rfile.read()
#     return data
#
#
# # Функция записи словаря степеней и коэффициентов в файл в виде многочлена
# def dictToFile(mydict, file3):
#     new_poly = ""
#     # идем в обратном порядке (не работает в python 3.6, нужна более новая версия)
#     for i in reversed(mydict.items()):
#         # если степень 0, то добавляем строку без X**0
#         if i[0] == 0:
#             new_poly += str(i[1]) + " + "
#         # иначе добавляем
#         else:
#             new_poly += str(i[1]) + "*x**" + str(i[0]) + " + "
#
#     # удаляем последние 3 символа (последние " + ")
#     new_poly = new_poly[:-3]
#
#     # записываем результат в файл
#     with open(file3, "w") as newfile:
#         print(f"Записываем в файл {file3} новый полином: {new_poly}")
#         newfile.write(new_poly)
#     return
#
#
# # парсим список и делаем из него словарь степеней и коэффициентов
# def makeDict(poly_list):
#     poly_dict = {}
#     # разворачиваем список
#     poly_list.reverse()
#     # идем по всему списку
#     for item in poly_list:
#         # если элемент последний, то проверяем, что там просто число, и добавляем его в словарь с индексом 0.
#         if item.isdigit():
#             poly_dict[0] = int(item)
#         # в противном случае парсим элемент списка на степень и коэффициент и пихаем их в словарь
#         else:
#             poly_dict[int(item.split("**")[-1])] = int(item[0:item.find("*")])
#     return poly_dict
#
#
# # Функция сложения двух словарей (значений по ключам) и возврата результата в первый словарь
# def sum_dict(dict1, dict2):
#     for key, value in dict1.items():
#         dict1[key] = value + dict2.get(key, 0)
#     return dict1
#
#
# def main():
#     # читаем первый многочлен из файла dz351.txt
#     poly1 = readFromFile("dz351.txt")
#     print("Полином 1:", poly1)
#     # читаем второй многочлен из файла dz352.txt
#     poly2 = readFromFile("dz352.txt")
#     print("Полином 2:", poly2)
#
#     print("Полином 1, преобразованный в список:", parse_poly(poly1))
#     print("Полином 2, преобразованный в список:", parse_poly(poly2))
#
#     # преобразовываем списки в словари
#     poly_dict1 = makeDict(parse_poly(poly1))
#     poly_dict2 = makeDict(parse_poly(poly2))
#
#     print("Парсим сумму полиномов в словарь:", sum_dict(poly_dict1, poly_dict2))
#
#     # записываем полученный многочлен в файл dz353.txt
#     dictToFile(poly_dict1, "dz353.txt")
#
#
# if __name__ == "__main__":
#     main()