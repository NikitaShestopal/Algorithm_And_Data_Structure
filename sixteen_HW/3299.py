MOD = 1_000_000_007
HASH_BASE = 33

class Tree:
    def __init__(self, num_nodes, parent_list):
        self.num_nodes = num_nodes
        self.parent = [-1] * num_nodes
        for i in range(1, num_nodes):
            self.parent[i] = parent_list[i - 1]

        self.children = [[] for _ in range(num_nodes)]
        for i in range(1, num_nodes):
            parent_index = self.parent[i]
            self.children[parent_index].append(i)

        self.depth = [0] * num_nodes
        self.max_log = 0
        self.ancestor_table = None

    def build_lifting_table(self):
        from collections import deque
        queue = deque([0])
        while queue:
            current = queue.popleft()
            for child in self.children[current]:
                self.depth[child] = self.depth[current] + 1
                queue.append(child)

        while (1 << self.max_log) <= self.num_nodes:
            self.max_log += 1

        self.ancestor_table = [[-1] * self.num_nodes for _ in range(self.max_log)]
        for i in range(self.num_nodes):
            self.ancestor_table[0][i] = self.parent[i]

        for j in range(1, self.max_log):
            for i in range(self.num_nodes):
                prev_ancestor = self.ancestor_table[j - 1][i]
                if prev_ancestor != -1:
                    self.ancestor_table[j][i] = self.ancestor_table[j - 1][prev_ancestor]

    def lowest_common_ancestor(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        depth_diff = self.depth[u] - self.depth[v]
        bit_position = 0
        while depth_diff:
            if depth_diff & 1:
                u = self.ancestor_table[bit_position][u]
            depth_diff //= 2
            bit_position += 1

        if u == v:
            return u

        for j in range(self.max_log - 1, -1, -1):
            if self.ancestor_table[j][u] != self.ancestor_table[j][v]:
                u = self.ancestor_table[j][u]
                v = self.ancestor_table[j][v]

        return self.parent[u]


if __name__ == '__main__':
    input_lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip():
            input_lines.append(line.strip())

    if not input_lines:
        exit()

    num_nodes, num_queries = map(int, input_lines[0].split())
    parent_list = list(map(int, input_lines[1].split())) if num_nodes > 1 else []

    initial_a1, initial_a2 = map(int, input_lines[2].split())
    x_coef, y_coef, z_coef = map(int, input_lines[3].split())

    tree = Tree(num_nodes, parent_list)
    tree.build_lifting_table()

    a = [0] * (2 * num_queries + 1)
    a[1], a[2] = initial_a1, initial_a2

    for i in range(3, 2 * num_queries + 1):
        a[i] = (x_coef * a[i - 2] + y_coef * a[i - 1] + z_coef) % num_nodes

    result = 0
    current_lca = tree.lowest_common_ancestor(a[1], a[2])
    result += current_lca
    last_lca = current_lca

    for i in range(2, num_queries + 1):
        u = (a[2 * i - 1] + last_lca) % num_nodes
        v = a[2 * i]
        current_lca = tree.lowest_common_ancestor(u, v)
        result += current_lca
        last_lca = current_lca

    print(result)
