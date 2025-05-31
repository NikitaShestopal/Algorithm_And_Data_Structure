def can_make_24(numbers):
    if len(numbers) == 1:
        return abs(numbers[0] - 24) < 1e-6

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num1 = numbers[i]
            num2 = numbers[j]

            remaining = [numbers[k] for k in range(len(numbers)) if k != i and k != j]

            possible_results = [
                num1 + num2,
                num1 - num2,
                num2 - num1,
                num1 * num2
            ]

            if abs(num2) > 1e-6:
                possible_results.append(num1 / num2)
            if abs(num1) > 1e-6:
                possible_results.append(num2 / num1)

            for result in possible_results:
                if can_make_24(remaining + [result]):
                    return True

    return False

if __name__ == '__main__':
    with open("input.txt") as input_file:
        test_cases = int(input_file.readline().strip())

        for _ in range(test_cases):
            line = input_file.readline().strip().split()
            numbers = [float(value) for value in line]
            if can_make_24(numbers):
                print("YES")
            else:
                print("NO")
