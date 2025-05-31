
def solve(current, used, n, k):
    if len(current) == k:
        print(" ".join(map(str, current)))
        return

    for i in range(1, n+1):
        if not used[i]:
            used[i] = True
            current.append(i)
            solve(current, used, n, k)
            current.pop()
            used[i] = False

if __name__ == '__main__':
    n, k = map(int, input().split())
    used = [False] * (n + 1)

    solve([], used, n, k)