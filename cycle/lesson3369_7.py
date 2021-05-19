'''
    https://stepik.org/lesson/3369/step/7?unit=952
'''

summ = 0
result = 0
list = []
while True:
    temp = int(input())
    summ += temp
    list.append(temp)
    if summ == 0:
        for i in list:
            result += i * i
        break


print(result)
