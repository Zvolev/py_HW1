""" Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
in
54
out
[2, 3, 3, 3]
in
9990
out
[2, 3, 3, 3, 5, 37]
in
650
out
[2, 5, 5, 13] """



def multi_list(num: int) -> list:
    multi_list = []
    for i in range(2, num):
        while num % i == 0:
            num = int(num / i)
            multi_list.append(i)
    return multi_list    
        
        
print(multi_list(int(input('add digit '))))
       