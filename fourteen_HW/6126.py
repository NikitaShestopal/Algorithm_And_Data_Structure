class Queue:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(int(value))
        return "ok"

    def pop(self):
        if not self._data:
            return "error"
        return self._data.pop(0)

    def front(self):
        if not self._data:
            return "error"
        return self._data[0]

    def size(self):
        return len(self._data)

    def clear(self):
        self._data.clear()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        parts = command.strip().split()
        cmd = parts[0]
        args = parts[1:]
        return getattr(self, cmd)(*args)


if __name__ == '__main__':
    queue = Queue()
    while True:
        try:
            line = input()
        except EOFError:
            break
        response = queue.execute(line)
        print(response)
        if response == "bye":
            break
