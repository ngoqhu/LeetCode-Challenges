def reverse(x):
    isNegative = False
    result = 0

    if x < 0:
        isNegative = True
        x *= -1

    while x >= 1:
        digit = x % 10
        x //= 10
        result = result * 10 + digit

    if result < pow(-2, 31) or result > pow(2, 31) - 1:
        return 0

    if isNegative:
        return -result
    else:
        return result
