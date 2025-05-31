class Variable:
    def __init__(self, name):
        self.name = name

class Addition:
    def __init__(self, left_expr, right_expr):
        self.left = left_expr
        self.right = right_expr

class Multiplication:
    def __init__(self, left_expr, right_expr):
        self.left = left_expr
        self.right = right_expr

def to_infix(expr_node, parent_precedence):
    if isinstance(expr_node, Variable):
        precedence = 3
        result = expr_node.name
    elif isinstance(expr_node, Multiplication):
        precedence = 2
        result = to_infix(expr_node.left, precedence) + to_infix(expr_node.right, precedence)
    elif isinstance(expr_node, Addition):
        precedence = 1
        result = to_infix(expr_node.left, precedence) + "+" + to_infix(expr_node.right, precedence)
    
    if precedence < parent_precedence:
        return f"({result})"
    else:
        return result

def parse_expression_full(expr_str, index):
    node, index = parse_product(expr_str, index)
    while index < len(expr_str) and expr_str[index] == '+':
        index += 1
        right_node, index = parse_product(expr_str, index)
        node = Addition(node, right_node)
    return node, index

def parse_product(expr_str, index):
    node, index = parse_factor(expr_str, index)
    while index < len(expr_str) and (expr_str[index].islower() or expr_str[index] == '('):
        right_node, index = parse_factor(expr_str, index)
        node = Multiplication(node, right_node)
    return node, index

def parse_factor(expr_str, index):
    if expr_str[index] == '(':
        index += 1
        node, index = parse_expression_full(expr_str, index)
        index += 1
        return node, index
    else:
        node = Variable(expr_str[index])
        index += 1
        return node, index

def parse(expr_str):
    node, _ = parse_expression_full(expr_str, 0)
    return node

def solve():
    try:
        while True:
            line = input()
            if line is None:
                break
            line = line.strip()
            if line == "":
                continue
            ast = parse(line)
            print(to_infix(ast, 0))
    except EOFError:
        return

if __name__ == '__main__':
    solve()
