class BubbleSorter:
    def __init__(self, arr):
        self.arr = arr
        self.swap_count = 0

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(n - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    self.swap_count += 1

    def get_swap_count(self):
        return self.swap_count

    def get_sorted_array(self):
        return self.arr


n = int(input())
arr = list(map(int, input().split()))

sorter = BubbleSorter(arr)
sorter.sort()

print(sorter.get_swap_count())
