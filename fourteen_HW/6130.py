class Deque:
    def __init__(self, capacity=4):
        self._buffer = [None] * capacity
        self._front_index = 0
        self._size = 0

    def _resize(self, new_capacity):
        new_buffer = [None] * new_capacity
        for i in range(self._size):
            new_buffer[i] = self._buffer[(self._front_index + i) % len(self._buffer)]
        self._buffer = new_buffer
        self._front_index = 0

    def push_back(self, item):
        if self._size == len(self._buffer):
            self._resize(len(self._buffer) * 2)
        back_index = (self._front_index + self._size) % len(self._buffer)
        self._buffer[back_index] = item
        self._size += 1
        return "ok"

    def push_front(self, item):
        if self._size == len(self._buffer):
            self._resize(len(self._buffer) * 2)
        self._front_index = (self._front_index - 1) % len(self._buffer)
        self._buffer[self._front_index] = item
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"
        item = self._buffer[self._front_index]
        self._front_index = (self._front_index + 1) % len(self._buffer)
        self._size -= 1
        return item

    def pop_back(self):
        if self._size == 0:
            return "error"
        back_index = (self._front_index + self._size - 1) % len(self._buffer)
        item = self._buffer[back_index]
        self._size -= 1
        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._buffer[self._front_index]

    def back(self):
        if self._size == 0:
            return "error"
        back_index = (self._front_index + self._size - 1) % len(self._buffer)
        return self._buffer[back_index]

    def size(self):
        return self._size

    def clear(self):
        self._buffer = [None] * 4
        self._front_index = 0
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        parts = command.strip().split()
        cmd = parts[0]
        args = parts[1:]
        if args:
            args = [int(x) if x.lstrip("-").isdigit() else x for x in args]
        return getattr(self, cmd)(*args)

if __name__ == '__main__':
    deque = Deque()
    with open("input.txt", "r") as file:
        for line in file:
            response = deque.execute(line.strip())
            print(response)
            if response == "bye":
                break
