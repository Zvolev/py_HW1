# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(raw_str):
    encoded = '' 
    prev_char = '' 
    count = 1
    # если строка пустая возвращаем пусто
    if not raw_str: 
        return '' 
    for char in raw_str: 
        # если текущий символ не совпадает с предыдущим
        if char != prev_char: 
            # тогда добаляем количество и символ
            if prev_char: 
                encoded += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            # иначе добавляем количество
            count += 1 
    else: 
        # закончили сжатие
        encoded += str(count) + prev_char 
    return encoded

def rle_decode(encodedstring):
    decode = ''
    count = ''
    for char in encodedstring:
        # если символ - цифра
        if char.isdigit():
            # добавляем к количеству
            count += char
        else:
            # иначе символ, значит записываем символ count раз
            decode += char * int(count)
            count = ''
    return decode

print()

compressed_text = rle_encode(input('Введите кодируюмую строку -> ')) #  
print()
print(f'Сжатие по алгоритму: {compressed_text}')
# результат записываем в файл
with open("coded_rle.txt", "w", encoding="utf-8") as my_f:
    my_f.write(compressed_text)

print()
# считываем из файла (, ранее закодированные данные) и раскодируем их
with open("coded_rle.txt") as my_f:
    compressed_text2 = my_f.readline()
print(f'Результат чтения из файла и раскодирования по алгоритму: {rle_decode(compressed_text2)}')
print()
