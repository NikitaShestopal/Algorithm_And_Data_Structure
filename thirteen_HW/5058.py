BRACKET_PAIRS = {"(": ")", "[": "]", "{": "}"}

def is_balanced_brackets(expression: str) -> bool:
    stack = []
    for current_bracket in expression:
        if current_bracket in BRACKET_PAIRS:
            stack.append(current_bracket)
        else:
            if not stack or BRACKET_PAIRS[stack.pop()] != current_bracket:
                return False
    return not stack

if __name__ == '__main__':
    bracket_sequence = input().strip()
    print("yes" if is_balanced_brackets(bracket_sequence) else "no")
