
# Напишите функцию, которая будет принимать координаты двух точек на плоскости
# и возвращать длину отрезка, соединяющего эти точки.
# Порядок передаваемых чисел — X, Y. Результат нужно округлить до сотых.
# Например:
# line_length([15, 7], [22, 11]) ➞ 8.06
# line_length([0, 0], [0, 0]) ➞ 0
# line_length([0, 0], [1, 1]) ➞ 1.41

import math
def length_line(x, y):
    a = y[0] - x[0]
    print(a)
    b = y[1] - x[1]
    print(b)
    line_c = math.sqrt(a ** 2 + b ** 2)
    return round(line_c, 2)

x1 = [15, 7]
y1 = [22, 11]

c1 = length_line(x1, y1)
print(c1)

# Вывод:
# 7
# 4
# 8.06


# Задачи с урока:

# В предложении были добавлены лишние пробелы между словами! Написать ф-цию,
# которая принимает такое предложение и возвращает его же в исправленном виде.

def correct_spacing(sent):
    result = sent.split()
    print(result)
    return result

sentence = input('Enter sentence: ')

result1 = correct_spacing(sentence)

print(' '.join(result1))

# Вывод:
# Enter sentence: The film       starts   at      midnight
# ['The', 'film', 'starts', 'at', 'midnight']
# The film starts at midnight


# Напишите ф-цию, которая принимает на вход целое число.
# Она должна возвращать True, если число является степенью числа 3.
# В противном случае вывести False.

def is_power_of_tree(num):

    if 3 ** num == 1:
        return True
    if num % 3 != 0:
        return False
    while num > 1:
        num = num / 3
        if num == 1:
            return True

    return False

n = int(input('Enter number: '))

print(is_power_of_tree(n))
