'''
https://stepik.org/lesson/3366/step/3?unit=949

Таблица умножения
Sample Input 3:

1
3
2
4

Sample Output 3:

	2	3	4
1	2	3	4
2	4	6	8
3	6	9	12

'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d+1):
    print("\t", i, end=" ")
print("\r")
for j in range(a, b + 1):
    print(j, end="")
    for i in range(c, d+1):
        print("\t", i * j, end=" ")
    print()
