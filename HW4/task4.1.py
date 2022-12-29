""" Вычислить число c заданной точностью d
in
Enter a real number: 9
Enter the required accuracy '0.0001': 0.000001

out
9.000000

in
Enter a real number: 8.98785
Enter the required accuracy '0.0001': 0.001

out
8.988 """



from decimal import Decimal
D = Decimal

num = float(input('Enter a real number: '))
d = float(input('Enter the required accuracy 0.0001: '))

print(D(str(num)).quantize(D(str(d))))  # quantize('0.0001') задаем шаблон округления
