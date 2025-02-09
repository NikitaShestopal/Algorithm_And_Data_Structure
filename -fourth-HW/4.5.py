def f(x):
    return x ** 3 + 4 * x ** 2 + x - 6


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


a, b = 0, 2
root = bisect_manual(a, b)
print(f"Корінь рівняння x^3 + 4x^2 + x - 6 = 0 на [0,2]: {root:.6f}")
#Відповідь 1.000000