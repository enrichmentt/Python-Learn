# https://stepik.org/lesson/3367/step/7?unit=950
# aaaabbсaa -> a4b2с1a2

s = input()
newStr = ""
counter = 1

for i in range(len(s)):
    if i < len(s) - 1:
        if s[i] == s[i + 1]:
            counter += 1
        else:
            newStr += s[i] + str(counter)
            counter = 1
    else:
        newStr += s[i] + str(counter)

print(newStr)
