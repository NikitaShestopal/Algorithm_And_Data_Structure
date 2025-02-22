def max_trucks(R, L, B, X):
    left = 0
    total_cost = 0
    max_trucks = 0

    for right in range(R):
        median = X[(left + right) // 2]
        total_cost += abs(X[right] - median)

        while total_cost > B:
            total_cost -= abs(X[left] - median)
            left += 1

        max_trucks = max(max_trucks, right - left + 1)

    return max_trucks

R, L, B = map(int, input().split())
X = [int(input()) for _ in range(R)]

print(max_trucks(R, L, B, X))