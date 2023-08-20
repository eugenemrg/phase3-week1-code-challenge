def positive_check(num1, num2, num3):
    pos = 0
    pos = pos + 1 if num1 > 0 else pos
    pos = pos + 1 if num2 > 0 else pos
    pos = pos + 1 if num3 > 0 else pos
    return pos > 1