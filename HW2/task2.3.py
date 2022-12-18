""" Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму. (1+\frac 1 n)^n
in
6

out
[2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
14.071 """

num = int(input('введите целое положительное число: '))

my_list = []
sum =0

for i in range(1, num+1):
    derivative = round((1 + 1/i)**i, 3)
    sum += derivative
    i +=1
    my_list.append(derivative)
    
print(my_list)
print(sum)
