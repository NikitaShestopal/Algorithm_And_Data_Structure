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

    def to_string(self):
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return " ".join(result)

    def rotate_right(self, k):
        if self.head is None or self.head.next is None:
            return
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        k %= length
        if k == 0:
            return
        current = self.head
        for _ in range(length - k - 1):
            current = current.next
        new_tail = current
        new_head = current.next
        self.tail.next = self.head
        new_tail.next = None
        self.head = new_head
        self.tail = new_tail


if __name__ == '__main__':
    num_elements = int(input())
    elements = list(map(int, input().split()))
    linked_list = LinkedList()
    for element in elements:
        linked_list.add_element(element)

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == "":
            continue
        k = int(line)
        linked_list.rotate_right(k)
        print(linked_list.to_string())
