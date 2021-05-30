# *numbers - произвольное количество аргументов
def min(*numbers):
    min = numbers[0]
    for number in numbers:
        if min > number:
            min = number
    return min


print(min(2, 3, 1, 4, 5, 6))
