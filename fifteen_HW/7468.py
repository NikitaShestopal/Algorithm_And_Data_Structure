class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def add_to_tail(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node

    def to_string(self) -> str:
        current_node = self.head
        result = []
        while current_node is not None:
            result.append(str(current_node.value))
            current_node = current_node.next
        return " ".join(result)

    def reverse_list(self, start_node: Node | None) -> Node | None:
        previous_node = None
        current_node = start_node
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node

    def reorder_list(self) -> None:
        if self.head is None or self.head.next is None:
            return

        slow_pointer = self.head
        fast_pointer = self.head
        first_half_end = None

        while fast_pointer is not None and fast_pointer.next is not None:
            first_half_end = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        if first_half_end is not None:
            first_half_end.next = None

        second_half = self.reverse_list(slow_pointer)
        first_half = self.head
        dummy_node = Node(0)
        merged_pointer = dummy_node

        while first_half is not None or second_half is not None:
            if first_half is not None:
                merged_pointer.next = first_half
                merged_pointer = merged_pointer.next
                first_half = first_half.next
            if second_half is not None:
                merged_pointer.next = second_half
                merged_pointer = merged_pointer.next
                second_half = second_half.next

        self.head = dummy_node.next

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        self.tail = current_node


if __name__ == '__main__':
    element_count = int(input())
    values = list(map(int, input().split()))
    linked_list = LinkedList()
    for value in values:
        linked_list.add_to_tail(value)
    linked_list.reorder_list()
    print(linked_list.to_string())
