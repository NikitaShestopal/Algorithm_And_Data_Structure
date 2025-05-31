class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_element(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_forward(self):
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return " ".join(result)

    def print_reverse(self):
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return " ".join(result[::-1])


if __name__ == '__main__':
    num_elements = int(input())
    elements = list(map(int, input().split()))
    linked_list = LinkedList()
    for element in elements:
        linked_list.add_element(element)
    print(linked_list.print_forward())
    print(linked_list.print_reverse())
