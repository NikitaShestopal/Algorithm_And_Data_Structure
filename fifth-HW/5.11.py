def max_trucks(R, L, B, X):
    prefix_sum = [0] * (R + 1)

    for i in range(R):
        prefix_sum[i + 1] = prefix_sum[i] + X[i]

    left = 0
    max_trucks = 0

    for right in range(R):
        median_idx = (left + right) // 2
        median = X[median_idx]

        left_cost = median * (median_idx - left) - (prefix_sum[median_idx] - prefix_sum[left])
        right_cost = (prefix_sum[right + 1] - prefix_sum[median_idx + 1]) - median * (right - median_idx)
        total_cost = left_cost + right_cost

        while total_cost > B:
            left += 1
            median_idx = (left + right) // 2
            median = X[median_idx]

            left_cost = median * (median_idx - left) - (prefix_sum[median_idx] - prefix_sum[left])
            right_cost = (prefix_sum[right + 1] - prefix_sum[median_idx + 1]) - median * (right - median_idx)
            total_cost = left_cost + right_cost

        max_trucks = max(max_trucks, right - left + 1)

    return max_trucks


R, L, B = map(int, input().split())
X = [int(input()) for _ in range(R)]

print(max_trucks(R, L, B, X))
