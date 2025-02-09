import math

def f(x):
    return math.sin(x) - x / 3

def bisect_manual(a, b, tol=1e-6):
    if f(a) * f(b) > 0:
        raise ValueError("Метод бісекції не застосовується: f(a) і f(b) мають однаковий знак")

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


a, b = 1.6, 3
root = bisect_manual(a, b)
print(f"Корінь рівняння sin(x) = x/3 на [1.6, 3]: {root:.6f}")
# Відповідь 2.278863