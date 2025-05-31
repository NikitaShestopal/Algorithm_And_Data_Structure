class BinarySearchTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def is_empty(self):
        return self.key is None

    def set_key(self, key):
        self.key = key

    def get_key(self):
        if self.is_empty():
            raise Exception("BinarySearchTree: дерево порожнє")
        return self.key

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def insert(self, key):
        if self.is_empty():
            self.set_key(key)
        else:
            current = self
            while True:
                if key == current.key:
                    break  # Ключ уже існує
                elif key < current.key:
                    if current.has_left():
                        current = current.left
                    else:
                        current.left = BinarySearchTree(key)
                        break
                else:  # key > current.key
                    if current.has_right():
                        current = current.right
                    else:
                        current.right = BinarySearchTree(key)
                        break

    def preorder_traversal(self):
        result = ""
        if not self.is_empty():
            result += self.get_key()
            if self.has_left():
                result += self.get_left().preorder_traversal()
            if self.has_right():
                result += self.get_right().preorder_traversal()
        return result


if __name__ == '__main__':
    input_lines = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == '*':
            break
        if line:
            input_lines.append(line)

    if input_lines:
        input_lines.reverse()
        root_key = input_lines[0][0]
        tree = BinarySearchTree(root_key)
        for round_str in input_lines[1:]:
            for char in round_str:
                tree.insert(char)
        print(tree.preorder_traversal())
