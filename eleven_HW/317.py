import sys
sys.set_int_max_str_digits(10**6)

def karatsuba(multiplicand1, multiplicand2):
    if multiplicand1 == "0" or multiplicand2 == "0":
        return "0"

    if len(multiplicand1) <= 64 and len(multiplicand2) <= 64:
        return str(int(multiplicand1) * int(multiplicand2))

    max_len = max(len(multiplicand1), len(multiplicand2))

    if max_len % 2 != 0:
        max_len += 1
    multiplicand1 = multiplicand1.zfill(max_len)
    multiplicand2 = multiplicand2.zfill(max_len)

    half_len = max_len // 2

    high1, low1 = multiplicand1[:-half_len], multiplicand1[-half_len:]
    high2, low2 = multiplicand2[:-half_len], multiplicand2[-half_len:]

    product_high = karatsuba(high1, high2)
    product_low = karatsuba(low1, low2)

    sum1 = str(int(high1) + int(low1))
    sum2 = str(int(high2) + int(low2))

    product_middle = karatsuba(sum1, sum2)
    product_middle = str(int(product_middle) - int(product_high) - int(product_low))

    final_result = int(product_high) * 10 ** (2 * half_len) + int(product_middle) * 10 ** half_len + int(product_low)
    return str(final_result)

if __name__ == '__main__':
    with open("input.txt") as input_file:
        for line in input_file:
            operands = line.split()
            number1 = operands[0]
            number2 = operands[1]
            multiplication_result = karatsuba(number1, number2)
            print(multiplication_result)

        input_file.close()
