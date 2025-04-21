class QuickSorter:
    def __init__(self, array):
        self.arr = array

    def sort(self):
        self._quick_sort(0, len(self.arr) - 1)

    def _quick_sort(self, left, right):
        if left >= right:
            return

        pivot = self.arr[(left + right) // 2]
        i, j = left, right

        while i <= j:
            while self.arr[i] < pivot:
                i += 1
            while self.arr[j] > pivot:
                j -= 1

            if i <= j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
                j -= 1

        self._quick_sort(left, j)
        self._quick_sort(i, right)

    def get_sorted(self):
        return self.arr


n = int(input())
numbers = list(map(int, input().split()))

sorter = QuickSorter(numbers)
sorter.sort()

print(*sorter.get_sorted())