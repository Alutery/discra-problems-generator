from math import factorial


def D(k):
    tmp = 0
    for i in range(k+1):
        tmp += (-1) ** i * factorial(k) / factorial(i)
    return tmp

print(D(1), D(5), D(4))