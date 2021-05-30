
def getValue():
    print(a)


a = 100  # global
getValue()  # 100


def getValue():
    a = 1  # local variable
    print(a)


a = 100  # global
getValue()  # 1
