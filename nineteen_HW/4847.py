class Heap:
    def __init__(self):
        self.heap = [None]
        self.size = 0
        self.id_to_index = {}

    def _add(self, element_id, priority):
        self.size += 1
        self.heap.append([priority, element_id])
        self.id_to_index[element_id] = self.size
        self.siftUp(self.size)

    def _pop(self):
        top_element = self.heap[1]
        self.id_to_index.pop(top_element[1])

        if self.size == 1:
            self.heap.pop()
            self.size -= 1
            return top_element

        self.heap[1] = self.heap[self.size]
        self.id_to_index[self.heap[1][1]] = 1
        self.heap.pop()
        self.size -= 1
        self.siftDown(1)
        return top_element

    def _change(self, element_id, new_priority):
        index = self.id_to_index.get(element_id)
        if index is None:
            return

        old_priority = self.heap[index][0]
        self.heap[index][0] = new_priority

        if new_priority > old_priority:
            self.siftUp(index)
        elif new_priority < old_priority:
            self.siftDown(index)

    def siftUp(self, index):
        while index > 1:
            parent = index // 2
            if self.heap[index][0] > self.heap[parent][0]:
                self.swap(index, parent)
            else:
                break
            index = parent

    def siftDown(self, index):
        while 2 * index <= self.size:
            left = 2 * index
            right = left + 1
            larger_child = left

            if right <= self.size and self.heap[right][0] > self.heap[left][0]:
                larger_child = right

            if self.heap[index][0] < self.heap[larger_child][0]:
                self.swap(index, larger_child)
                index = larger_child
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.id_to_index[self.heap[i][1]] = i
        self.id_to_index[self.heap[j][1]] = j


if __name__ == '__main__':
    heap = Heap()
    result = []

    try:
        while True:
            line = input().strip()
            if not line:
                continue

            parts = line.split()
            command = parts[0]

            if command == 'ADD':
                element_id = parts[1]
                priority = int(parts[2])
                heap._add(element_id, priority)

            elif command == 'POP':
                popped = heap._pop()
                result.append(f'{popped[1]} {popped[0]}')

            elif command == 'CHANGE':
                element_id = parts[1]
                new_priority = int(parts[2])
                heap._change(element_id, new_priority)

    except EOFError:
        pass

    for line in result:
        print(line)

