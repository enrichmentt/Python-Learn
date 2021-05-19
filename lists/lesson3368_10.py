'''
    https://stepik.org/lesson/3368/step/10?unit=951

    Sample Input 1:

    1 3 5 6 10
    Sample Output 1:

    13 6 9 15 7
'''

list = [int(i) for i in input().split()]
res = ""
index_middle = 0

while index_middle < len(list):
    if len(list) == 1:
        print(list[0])
        break

    index_first = index_middle - 1
    index_second = index_middle + 1

    if index_middle == len(list) - 1:
        index_second = 0

    print(list[index_first] + list[index_second], end=" ")
    index_middle += 1
