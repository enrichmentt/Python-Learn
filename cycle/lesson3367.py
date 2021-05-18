str = input()
per = (str.upper().count('c'.upper()) +
       str.upper().count('g'.upper())) / 10 * 100
print(per)
