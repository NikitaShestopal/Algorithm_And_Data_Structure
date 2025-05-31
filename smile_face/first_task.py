n = int(input())
board = [list(input().strip()) for _ in range(n)]

points = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '@':
            points.append((i, j))
            
start, end = points

queue = [(start[0], start[1], [])]
visited = [[False]*n for _ in range(n)]
visited[start[0]][start[1]] = True

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

found = False
path = []

while queue:
    x, y, current_path = queue[0]
    queue = queue[1:]
    if (x, y) == end:
        path = current_path + [(x, y)]
        found = True
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if board[nx][ny] != "#":
                visited[nx][ny] = True
                queue.append((nx, ny, current_path + [(x, y)]))

if not found:
    print("Impossible")
else:
    for (x,y) in path:
        if board[x][y] == '.':
            board[x][y] = '@'
    for row in board:
        print(''.join(row))