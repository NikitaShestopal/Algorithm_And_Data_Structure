class BinarySearchTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def is_empty(self):
        return self.key is None

    def set_key(self, value):
        self.key = value

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
                if key < current.key:
                    if current.has_left():
                        current = current.left
                    else:
                        current.left = BinarySearchTree(key)
                        break
                else:
                    if current.has_right():
                        current = current.right
                    else:
                        current.right = BinarySearchTree(key)
                        break

    def is_same_tree(self, other):
        if self.is_empty() and (other is None or other.is_empty()):
            return 1

        if self.is_empty() or other is None or other.is_empty():
            return 0

        if self.key != other.key:
            return 0

        if self.has_left() and other.has_left():
            left_same = self.get_left().is_same_tree(other.get_left())
        elif not self.has_left() and not other.has_left():
            left_same = 1
        else:
            left_same = 0

        if self.has_right() and other.has_right():
            right_same = self.get_right().is_same_tree(other.get_right())
        elif not self.has_right() and not other.has_right():
            right_same = 1
        else:
            right_same = 0

        return 1 if left_same and right_same else 0


if __name__ == '__main__':
    n = int(input().strip())
    values1 = list(map(int, input().split()))
    tree1 = BinarySearchTree()
    for val in values1:
        tree1.insert(val)

    m = int(input().strip())
    values2 = list(map(int, input().split()))
    tree2 = BinarySearchTree()
    for val in values2:
        tree2.insert(val)

    print(tree1.is_same_tree(tree2))
