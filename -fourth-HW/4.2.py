def sqrt(n:float):
    res = 0
    bit = 1 << 15

    while bit > 0:
        temp = res | bit
        if temp * temp <= n:
            res = temp
        bit >>= 1

    return res

n = float(input())
print(f"{sqrt(n):.10f}")