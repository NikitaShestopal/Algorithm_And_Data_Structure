def sqrt(n: float):
    if n == 0:
        return 0.0
    x = n
    while True:
        next_x = 0.5 * (x + n / x)
        if abs(next_x - x) < 1e-6:
            break
        x = next_x

    return x

n = float(input())
print(f"{sqrt(n):.6f}")
