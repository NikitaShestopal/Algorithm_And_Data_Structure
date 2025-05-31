def has_cycle(n, matrix):
    visited = [0] * n

    def dfs(v):
        visited[v] = 1
        for u in range(n):
            if matrix[v][u]:
                if visited[u] == 1:
                    return True
                if visited[u] == 0 and dfs(u):
                    return True
        visited[v] = 2
        return False

    for i in range(n):
        if visited[i] == 0:
            if dfs(i):
                return 1
    return 0

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(has_cycle(n, matrix))