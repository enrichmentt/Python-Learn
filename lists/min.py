﻿'''
    поиск минимума
'''
print("Введите числа через пробел:")
numbers = [int(i) for i in input().split()]
min = numbers[0]

for number in numbers:
    if min > number:
        min = number
print(min)
