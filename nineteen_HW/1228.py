class Heap:
    def __init__(self):
        self.data = [0]
        self.count = 0

    def insert(self, value):
        self.count += 1
        self.data.append(value)
        self.sift_up()

    def sift_up(self):
        index = self.count

        while index > 1:
            parent_index = index // 2

            if self.data[index] < self.data[parent_index]:
                self.swap(index, parent_index)
            else:
                break
            index = parent_index

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def extract_min(self):
        min_value = self.data[1]
        self.data[1] = self.data[self.count]
        self.data.pop()
        self.count -= 1
        self.sift_down()
        return min_value

    def sift_down(self):
        index = 1

        while 2 * index <= self.count:
            left = 2 * index
            right = left + 1
            smallest = left

            if right <= self.count and self.data[right] < self.data[left]:
                smallest = right

            if self.data[index] > self.data[smallest]:
                self.swap(index, smallest)
                index = smallest
            else:
                break

if __name__ == '__main__':
    n = int(input().strip())
    elements = list(map(int, input().split()))
    heap = Heap()

    for element in elements:
        heap.insert(element)

    total_cost = 0
    while heap.count > 1:
        first = heap.extract_min()
        second = heap.extract_min()
        merged = first + second
        total_cost += merged
        heap.insert(merged)

    print(total_cost)
