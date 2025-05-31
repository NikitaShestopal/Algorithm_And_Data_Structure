class Stack:
    def __init__(self, max_size=100):
        self.elements = [0 for _ in range(max_size)]
        self.top_index = -1

    def push(self, value):
        self.top_index += 1
        self.elements[self.top_index] = value
        return 'ok'

    def pop(self):
        if self.top_index < 0:
            return 'error'
        value = self.elements[self.top_index]
        self.top_index -= 1
        return value

    def size(self):
        return self.top_index + 1

    def back(self):
        if self.top_index < 0:
            return 'error'
        return self.elements[self.top_index]

    def clear(self):
        self.__init__(len(self.elements))
        return 'ok'

    def exit(self):
        return 'bye'

    def execute(self, command):
        command_name, *arguments = command.strip().split()
        return getattr(self, command_name)(*arguments)

if __name__ == '__main__':
    with open("input.txt") as input_file:
        stack = Stack()
        for line in input_file:
            result = stack.execute(line)
            print(result)
            if result == 'bye':
                break