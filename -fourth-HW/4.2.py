def sqrt(n: float, eps: float = 1e-6) -> float:
    if n == 0:
        return 0.0

    left, right = 0, max(1, n)
    while right - left > eps:
        mid = (left + right) / 2
        if mid * mid < n:
            left = mid
        else:
            right = mid

    return (left + right) / 2


n = float(input())
print(f"{round(sqrt(n)):.9f}")
