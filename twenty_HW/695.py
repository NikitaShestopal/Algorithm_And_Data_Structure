class SegmentTree:
    def __init__(self, length):
        size = 1
        while size < length:
            size <<= 1
        self.size = size
        self.min_tree = [10**18] * (2 * size)
        self.max_tree = [-10**18] * (2 * size)

    def build(self, array):
        for i, val in enumerate(array):
            self.min_tree[self.size + i] = val
            self.max_tree[self.size + i] = val
        for i in range(self.size - 1, 0, -1):
            self.min_tree[i] = min(self.min_tree[2 * i], self.min_tree[2 * i + 1])
            self.max_tree[i] = max(self.max_tree[2 * i], self.max_tree[2 * i + 1])

    def update(self, position, value):
        i = position + self.size
        self.min_tree[i] = value
        self.max_tree[i] = value
        i //= 2
        while i > 0:
            self.min_tree[i] = min(self.min_tree[2 * i], self.min_tree[2 * i + 1])
            self.max_tree[i] = max(self.max_tree[2 * i], self.max_tree[2 * i + 1])
            i //= 2

    def query(self, left, right):
        l = left + self.size
        r = right + self.size
        current_min = 10**18
        current_max = -10**18
        while l <= r:
            if l & 1:
                current_min = min(current_min, self.min_tree[l])
                current_max = max(current_max, self.max_tree[l])
                l += 1
            if not (r & 1):
                current_min = min(current_min, self.min_tree[r])
                current_max = max(current_max, self.max_tree[r])
                r -= 1
            l //= 2
            r //= 2
        return current_min, current_max


if __name__ == "__main__":
    query_count = int(input())
    max_length = 100_000

    data = [0] * max_length
    for i in range(max_length):
        n = i + 1
        data[i] = (n * n) % 12345 + (n * n * n) % 23456

    segment_tree = SegmentTree(max_length)
    segment_tree.build(data)

    output = []
    for _ in range(query_count):
        x, y = map(int, input().split())
        if x > 0:
            left = x - 1
            right = y - 1
            minimum, maximum = segment_tree.query(left, right)
            output.append(str(maximum - minimum))
        else:
            index = -x - 1
            segment_tree.update(index, y)

    print('\n'.join(output))
