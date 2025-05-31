max_value: int

def solve(i, current):
    global max_value
    if max_value == N:
        return

    if i == len(tracks):
        if current > max_value:
            max_value = current
        return

    solve(i + 1, current)
    if current + tracks[i] <= N:
        solve(i + 1, current + tracks[i])


if __name__ == '__main__':
    with open("input.txt") as f:
        for line in f:
            data = list(map(int, line.split()))
            N = data[0]
            s = data[1]
            tracks = data[2:]
            max_value = 0

            solve(0, 0)
            print(f"sum:" + str(max_value))
        f.close()