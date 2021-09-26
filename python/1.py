def tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == "__main__":
    import sys
    print(tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))

    