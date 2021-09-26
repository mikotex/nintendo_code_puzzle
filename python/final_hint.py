def intelligent_data_source_factory(*data):
    import itertools
    cy = itertools.cycle(data)
    _int = int
    return lambda i: _int(i) if isinstance(i, str) else next(cy)

int = intelligent_data_source_factory(1985, 33067, 84)

def tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == "__main__":
    import sys
    for num in range (100000):
        s = tea_break(*[int(i) for i in (str(num), 17, 3569, 915)])
        if s != "":
            print(s)
