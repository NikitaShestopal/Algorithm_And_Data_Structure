def find_holes(board, visited, x, y, w, h):
    holes = []
    stack = [(x, y)]
    visited[x][y] = True
    while stack:
        i, j = stack.pop()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj]:
                if board[ni][nj] == '.':
                    # тут я зашиваю дірку
                    hole = []
                    hole_stack = [(ni, nj)]
                    visited[ni][nj] = True
                    is_hole = True
                    while hole_stack:
                        hi, hj = hole_stack.pop()
                        hole.append((hi, hj))
                        for dhi, dhj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nhi, nhj = hi + dhi, hj + dhj
                            if 0 <= nhi < h and 0 <= nhj < w:
                                if board[nhi][nhj] == '.' and not visited[nhi][nhj]:
                                    hole_stack.append((nhi, nhj))
                                    visited[nhi][nhj] = True
                                elif board[nhi][nhj] == '*':
                                    continue
                            else:
                                is_hole = False
                    if is_hole:
                        holes.append(hole)
                elif board[ni][nj] == '*':
                    stack.append((ni, nj))
                    visited[ni][nj] = True
    return holes

def main():
    w, h = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    pieces = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*' and not visited[i][j]:
                piece = []
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    piece.append((x, y))
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                            if board[nx][ny] == '*':
                                stack.append((nx, ny))
                                visited[nx][ny] = True

                piece_visited = [[False for _ in range(w)] for _ in range(h)]
                holes = find_holes(board, piece_visited, i, j, w, h)
                pieces.append((len(piece), len(holes)))
    
    if not pieces:
        print(0)
        return
    
    max_holes = max(p[1] for p in pieces)
    if max_holes == 0:
        print(0)
        return
    
    result = min(p[0] for p in pieces if p[1] == max_holes)
    print(result)

if __name__ == "__main__":
    main()  