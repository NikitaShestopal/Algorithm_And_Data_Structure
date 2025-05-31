class Stack:
    def __init__(self, max_size=1000):
        self.elements = [0 for _ in range(max_size)]
        self.top_index = -1

    def push(self, value):
        self.top_index += 1
        self.elements[self.top_index] = value
        return 'ok'

    def pop(self):
        value = self.elements[self.top_index]
        self.top_index -= 1
        return value

    def back(self):
        return self.elements[self.top_index]

    def size(self):
        return self.top_index + 1

    def clear(self):
        self.__init__(len(self.elements))
        return 'ok'

    def exit(self):
        return 'bye'

    def execute(self, command):
        method_name, *arguments = command.strip()
        return getattr(self, method_name)(*arguments)


def can_achieve_permutation(train_count, target_order):
    station_stack = Stack(max_size=train_count + 5)
    incoming_train = 1

    for needed_train in target_order:
        while incoming_train <= train_count and (station_stack.size() == 0 or station_stack.back() != needed_train):
            station_stack.push(incoming_train)
            incoming_train += 1
        if station_stack.back() == needed_train:
            station_stack.pop()
        else:
            return False
    return True


if __name__ == '__main__':
    with open("input.txt") as input_file:
        lines = [line.strip() for line in input_file if line.strip()]
        line_index = 0

        while line_index < len(lines):
            train_count = int(lines[line_index])
            line_index += 1

            if train_count == 0:
                break

            while True:
                if line_index >= len(lines):
                    break

                line = lines[line_index]
                line_index += 1

                if line == '0':
                    print()
                    break

                desired_order = list(map(int, line.split()))
                result = 'Yes' if can_achieve_permutation(train_count, desired_order) else 'No'
                print(result)
