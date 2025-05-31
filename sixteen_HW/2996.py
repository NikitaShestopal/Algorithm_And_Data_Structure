class TreeNode:
    def __init__(self, id_: int, bribe: int):
        self.id = id_
        self.bribe = bribe
        self.children: list[TreeNode] = []

    def add_child(self, child: 'TreeNode') -> None:
        self.children.append(child)


def compute_min_cost(node: TreeNode) -> int:
    if not node.children:
        return node.bribe
    return node.bribe + min(compute_min_cost(child) for child in node.children)


if __name__ == '__main__':
    num_nodes = int(input().strip())

    nodes: dict[int, TreeNode] = {i: TreeNode(i, 0) for i in range(1, num_nodes + 1)}
    child_map: dict[int, list[int]] = {}

    for i in range(1, num_nodes + 1):
        parts = input().split()
        bribe_amount = int(parts[0])
        num_children = int(parts[1])
        child_ids = list(map(int, parts[2:2 + num_children])) if num_children > 0 else []

        nodes[i].bribe = bribe_amount
        child_map[i] = child_ids

    for parent_id, children_ids in child_map.items():
        for child_id in children_ids:
            nodes[parent_id].add_child(nodes[child_id])

    root = nodes[1]
    result = compute_min_cost(root)
    print(result)
