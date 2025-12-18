import re

def read_grid(filename="input.txt"):
    lines = [line.rstrip("\n") for line in open(filename)]
    width = max(len(l) for l in lines)
    return [l.ljust(width) for l in lines]

def locate_blocks(lines):
    R, C = len(lines), len(lines[0])
    blank = [all(lines[r][c] == ' ' for r in range(R)) for c in range(C)]
    blocks = []
    c = 0
    while c < C:
        if blank[c]:
            c += 1
            continue
        start = c
        while c < C and not blank[c]:
            c += 1
        blocks.append((start, c - 1))
    return blocks

def solve(filename="input day 6.txt"):
    lines = read_grid(filename)
    R = len(lines)
    blocks = locate_blocks(lines)
    total = 0

    for start, end in blocks:
        cols = list(range(start, end + 1))

        op = '*' if '*' in lines[-1][start:end+1] else '+'
        values = []

        for c in reversed(cols):
            digits = []
            for r in range(R - 1):  
                if lines[r][c].isdigit():
                    digits.append(lines[r][c])
            if digits:
                values.append(int("".join(digits)))

        if op == '+':
            total += sum(values)
        else:
            prod = 1
            for v in values:
                prod *= v
            total += prod

    print(total)

if __name__ == "__main__":
    solve()
