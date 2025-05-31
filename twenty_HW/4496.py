class SegmentTree:
    def __init__(self, data):
        self.length = len(data)
        size = 1
        while size < self.length:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * self.size)
        for i, val in enumerate(data):
            self.tree[self.size + i] = val
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, position, value):
        i = position + self.size
        self.tree[i] = value
        i //= 2
        while i > 0:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def find_prefix(self, capacity):
        if self.tree[1] <= capacity:
            return self.length
        idx = 1
        while idx < self.size:
            left_sum = self.tree[2 * idx]
            if left_sum > capacity:
                idx = 2 * idx
            else:
                capacity -= left_sum
                idx = 2 * idx + 1
        return idx - self.size


if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))
    m = int(input())
    segment_tree = SegmentTree(weights)
    results = []
    for _ in range(m):
        parts = input().split()
        query_type = int(parts[0])
        if query_type == 1:
            value = int(parts[1])
            count = segment_tree.find_prefix(value)
            results.append(str(count))
        else:
            index = int(parts[1]) - 1
            new_value = int(parts[2])
            segment_tree.update(index, new_value)
    print("\n".join(results))
