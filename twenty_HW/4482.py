import math

class SegmentTree:
    def __init__(self, values):
        length = len(values)
        size = 1 << math.ceil(math.log2(length)) if length > 1 else 1
        self.size = size
        self.tree = [(0, 1)] * (2 * size)

        for i, val in enumerate(values):
            self.tree[size + i] = (val, val)

        for i in range(size - 1, 0, -1):
            gcd_left, lcm_left = self.tree[2 * i]
            gcd_right, lcm_right = self.tree[2 * i + 1]
            gcd_val = math.gcd(gcd_left, gcd_right)
            lcm_val = (lcm_left // math.gcd(lcm_left, lcm_right)) * lcm_right
            self.tree[i] = (gcd_val, lcm_val)

    def update(self, position, value):
        idx = (position - 1) + self.size
        self.tree[idx] = (value, value)
        idx //= 2
        while idx > 0:
            gcd_left, lcm_left = self.tree[2 * idx]
            gcd_right, lcm_right = self.tree[2 * idx + 1]
            gcd_val = math.gcd(gcd_left, gcd_right)
            lcm_val = (lcm_left // math.gcd(lcm_left, lcm_right)) * lcm_right
            self.tree[idx] = (gcd_val, lcm_val)
            idx //= 2

    def query(self, left, right):
        l = (left - 1) + self.size
        r = (right - 1) + self.size
        gcd_result = 0
        lcm_result = 1
        while l <= r:
            if l & 1:
                gcd_val, lcm_val = self.tree[l]
                gcd_result = math.gcd(gcd_result, gcd_val)
                lcm_result = (lcm_result // math.gcd(lcm_result, lcm_val)) * lcm_val
                l += 1
            if not (r & 1):
                gcd_val, lcm_val = self.tree[r]
                gcd_result = math.gcd(gcd_result, gcd_val)
                lcm_result = (lcm_result // math.gcd(lcm_result, lcm_val)) * lcm_val
                r -= 1
            l //= 2
            r //= 2
        return gcd_result, lcm_result


if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split()))
    queries_count = int(input())
    segment_tree = SegmentTree(values)
    results = []
    for _ in range(queries_count):
        q, left, right = input().split()
        q = int(q)
        left = int(left)
        right = int(right)
        if q == 1:
            gcd_val, lcm_val = segment_tree.query(left, right)
            if gcd_val < lcm_val:
                results.append("wins")
            elif gcd_val > lcm_val:
                results.append("loser")
            else:
                results.append("draw")
        elif q == 2:
            segment_tree.update(left, right)
    print("\n".join(results))
