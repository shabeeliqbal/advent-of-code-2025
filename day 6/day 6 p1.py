import re

def read_grid(filename="input.txt"):
    lines = [line.rstrip("\n") for line in open(filename)]
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]
    return lines

def find_blocks(lines):
    rows = len(lines)
    cols = len(lines[0])
    blank_col = []
    for c in range(cols):
        blank_col.append(all(lines[r][c] == ' ' for r in range(rows)))

    blocks = []
    c = 0
    while c < cols:
        if blank_col[c]:
            c += 1
            continue
        start = c
        while c < cols and not blank_col[c]:
            c += 1
        end = c - 1
        blocks.append((start, end))
    return blocks

def solve(filename="input day 6.txt"):
    lines = read_grid(filename)
    rows = len(lines)
    blocks = find_blocks(lines)
    total = 0

    for start, end in blocks:
        nums = []
        for r in range(rows - 1):
            segment = ''.join(lines[r][start:end+1])
            m = re.search(r'\d+', segment)
            if m:
                nums.append(int(m.group(0)))

        op_row = ''.join(lines[-1][start:end+1])
        op = '+' if '+' in op_row else '*'

        if op == '+':
            val = sum(nums)
        else:
            val = 1
            for n in nums:
                val *= n

        total += val

    print(total)

if __name__ == "__main__":
    solve()
