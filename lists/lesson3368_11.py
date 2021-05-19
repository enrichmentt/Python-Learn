'''
    https://stepik.org/lesson/3368/step/11?unit=951

    Sample Input 1:

    4 8 0 3 4 2 0 3
    0 0 2 3 3 4 4 8 <- sort
    Sample Output 1:

    0 3 4
'''

list = [int(i) for i in input().split()]
list.sort()
result = []
counter = 0

for i in range(len(list)):
    if list.count(list[i]) >= 2:
        result.append(list[i])

print(*set(result))
