class TreeNode:
    def __init__(self, name: str):
        self.name = name
        self.children: dict[str, TreeNode] = {}

    def add_path(self, path_parts: list[str]) -> None:
        if not path_parts:
            return
        current_part = path_parts[0]
        if current_part not in self.children:
            self.children[current_part] = TreeNode(current_part)
        self.children[current_part].add_path(path_parts[1:])

    def print_tree(self, depth: int = 0) -> None:
        if self.name != "":
            print(" " * depth + self.name)
        for child_name in sorted(self.children.keys()):
            self.children[child_name].print_tree(depth + 1)


if __name__ == '__main__':
    num_paths = int(input().strip())
    root = TreeNode("")

    for _ in range(num_paths):
        raw_path = input().strip()
        path_parts = raw_path.split("\\")
        root.add_path(path_parts)

    for top_level_key in sorted(root.children.keys()):
        root.children[top_level_key].print_tree(0)