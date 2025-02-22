def can_process_in_time(T, N, Na, A, Nb, B):
    total_A = sum(T // a for a in A)
    total_B = sum(T // b for b in B)
    return min(total_A, total_B) >= N

def min_processing_time(N, Na, A, Nb, B):
    left, right = 1, 10**9
    while left <= right:
        mid = (left + right) // 2
        if can_process_in_time(mid, N, Na, A, Nb, B):
            right = mid - 1
        else:
            left = mid + 1
    return left

N = int(input())
Na = int(input())
A = list(map(int, input().split()))
Nb = int(input())
B = list(map(int, input().split()))

print(min_processing_time(N, Na, A, Nb, B))
