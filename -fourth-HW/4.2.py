import math


def f(x):
    return x * x + math.sqrt(x)


def done():
    c = float(input())
    left, right = 0, c

    while right - left > 1e-10:
        middle = (left + right) / 2
        y = f(middle)
        if y > c:
            right = middle
        else:
            left = middle

    print(left)

done()