def convert_base(number_str: str, source_base: int, target_base: int) -> str:
    decimal_value = 0
    for digit_char in number_str:
        decimal_value = decimal_value * source_base + int(digit_char)

    if decimal_value == 0:
        return "0"

    converted_digits = []
    while decimal_value > 0:
        converted_digits.append(decimal_value % target_base)
        decimal_value //= target_base

    result = ""
    while converted_digits:
        result += format_digit(converted_digits.pop())

    return result

def format_digit(digit: int) -> str:
    if digit < 10:
        return str(digit)
    else:
        return f"[{digit}]"

if __name__ == '__main__':
    input_number = input().strip()
    target_base = int(input().strip())
    print(convert_base(input_number, 10, target_base))
