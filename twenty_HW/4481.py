from math import log2, gcd

class SegmentTree:
    def __init__(self, data):
        length = len(data)
        if length == 1:
            size = 1
        else:
            size = 1 << (int(log2(length - 1)) + 1)

        self.tree = [0] * (2 * size)

        for i in range(length):
            self.tree[size + i] = data[i]

        for i in range(size - 1, 0, -1):
            self.tree[i] = gcd(self.tree[2 * i], self.tree[2 * i + 1])

        self.size = size

    def update(self, index, value):
        index += self.size
        self.tree[index] = value

        parent = index // 2
        while parent > 0:
            self.tree[parent] = gcd(self.tree[2 * parent], self.tree[2 * parent + 1])
            parent //= 2

    def query(self, left, right):
        left += self.size
        right += self.size

        result = 0
        while left <= right:
            if left & 1:
                result = gcd(result, self.tree[left])
                left += 1
            if not (right & 1):
                result = gcd(result, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return result

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    queries_count = int(input())
    segment_tree = SegmentTree(array)

    for _ in range(queries_count):
        parts = input().split()
        op = parts[0]
        l = int(parts[1]) - 1
        r = int(parts[2]) - 1
        if op == '1':
            print(segment_tree.query(l, r))
        else:
            segment_tree.update(l, r + 1)
