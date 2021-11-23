from decimal import *
from math import factorial

AC = 100
N = 4


def pi(N):
    pi = Decimal(0)
    k = 0
    while k < AC:
        pi += (Decimal(-1) ** k) * (Decimal(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k))) * (
                13591409 + 545140134 * k) / (640320 ** (3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi ** (-1)
    return round(pi, N)


# test

getcontext().prec = AC
print(pi(N), '\n>> Точность:', AC, '\n>> Количество знаков:', N)
