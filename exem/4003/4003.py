class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def Insert(self, val: int) -> None:
        if self.head is None:
            self.head = TreeNode(val)
        else:
            self._insert(self.head, val)

    def _insert(self, node: TreeNode, val: int) -> None:
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

    def SumLeft(self) -> int:
        return self._sum_left_leaves(self.head)

    def _sum_left_leaves(self, node: TreeNode) -> int:
        if node is None:
            return 0

        sum_left = 0
        if node.left:
            if node.left.left is None and node.left.right is None:
                sum_left += node.left.val
            else:
                sum_left += self._sum_left_leaves(node.left)

        sum_left += self._sum_left_leaves(node.right)
        return sum_left

n = int(input())
values = list(map(int, input().split()))

tree = Tree()
for val in values:
    tree.Insert(val)

print(tree.SumLeft())
