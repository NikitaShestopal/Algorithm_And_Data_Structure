OPERATOR_PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}

def prefix_to_infix(expression: str, index: int):
    current_token = expression[index]

    if current_token.isalpha():
        return current_token, 3, index + 1

    operator = current_token
    current_precedence = OPERATOR_PRECEDENCE[operator]

    left_expr, left_precedence, next_index = prefix_to_infix(expression, index + 1)
    right_expr, right_precedence, next_index = prefix_to_infix(expression, next_index)

    if left_precedence < current_precedence:
        left_expr = f"({left_expr})"
    if right_precedence < current_precedence or (
        right_precedence == current_precedence and operator in "-/"
    ):
        right_expr = f"({right_expr})"

    return f"{left_expr}{operator}{right_expr}", current_precedence, next_index

if __name__ == '__main__':
    prefix_expr = input().strip()
    infix_expr, _, _ = prefix_to_infix(prefix_expr, 0)
    print(infix_expr)
