"""
    https://stepik.org/lesson/3372/step/9?unit=955

    Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
    lst = [1, 2, 3, 4, 5, 6]
    print(modify_list(lst))  # None
    print(lst)               # [1, 2, 3]
    modify_list(lst)
    print(lst)               # [1]

    lst = [10, 5, 8, 3]
    modify_list(lst)
    print(lst)               # [5, 4]
"""

#lst = [1, 1, 3, 2, 4, 5, 6, 8, -1, 7, 8, 9, -16, 0, 4]
lst = [5, 3, 1]


def modify_list(l):
    i = len(l) - 1
    while i >= 0:
        if l[i] % 2 != 0:
            l.remove(l[i])
        else:
            l[i] = (int)(l[i] / 2)
        i -= 1


print(modify_list(lst))
