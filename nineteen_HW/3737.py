class MinHeap:
    def __init__(self, elements):
        self.data = [0] + elements
        self.size = len(elements)

    def is_valid_min_heap(self):
        for i in range(1, self.size + 1):
            left_child = 2 * i
            right_child = 2 * i + 1

            if left_child <= self.size and self.data[i] > self.data[left_child]:
                return False
            if right_child <= self.size and self.data[i] > self.data[right_child]:
                return False
        return True

if __name__ == '__main__':
    n = int(input().strip())
    elements = list(map(int, input().split()))
    min_heap = MinHeap(elements)
    print('YES' if min_heap.is_valid_min_heap() else 'NO')
