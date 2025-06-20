from collections import deque

def read_input():
    import sys
    input = sys.stdin.read
    data = input().split()
    M, N = int(data[0]), int(data[1])
    grid = [list(data[i + 2]) for i in range(M)]
    return M, N, grid

def solve(M, N, grid):
    visited = [[False] * N for _ in range(M)]
    max_area = 0
    num_blots = 0

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        area = 1
        while q:
            cx, cy = q.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[nx][ny] and grid[nx][ny] == '1':
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        area += 1
        return area

    for i in range(M):
        for j in range(N):
            if grid[i][j] == '1' and not visited[i][j]:
                blot_area = bfs(i, j)
                num_blots += 1
                max_area = max(max_area, blot_area)

    print(num_blots, max_area)

M, N, grid = read_input()
solve(M, N, grid)
