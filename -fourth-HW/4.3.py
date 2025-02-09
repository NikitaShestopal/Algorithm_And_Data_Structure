def f(x):
    return x ** 3 + x - 4

def bisect_manual(a, b, eps=1e-6):
    if f(a) * f(b) > 0:
        raise ValueError("Метод бісекції не застосовується: f(a) і f(b) мають однаковий знак")

    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


a, b = 0, 10
x_min = bisect_manual(a, b)
print(f"Найменше x, для якого f(x) > 5: {x_min}")
# Відповідь 1.3787966966629028
