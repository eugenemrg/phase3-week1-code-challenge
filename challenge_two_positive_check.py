def positive_check(a, b, c):
    pos = 0
    pos = pos + 1 if a > 0 else pos
    pos = pos + 1 if b > 0 else pos
    pos = pos + 1 if c > 0 else pos
    return pos > 1