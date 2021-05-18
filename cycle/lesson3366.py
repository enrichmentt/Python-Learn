'''

https://stepik.org/lesson/3366/step/7?unit=949

'''

a = int(input())
b = int(input())
counter = 0
result = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        result += i
        counter += 1

print(result / counter)
