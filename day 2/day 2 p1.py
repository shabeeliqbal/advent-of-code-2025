def parse_ranges(line):
    ranges = []
    for part in line.strip().split(','):
        if not part:
            continue
        a, b = part.split('-')
        ranges.append((int(a), int(b)))
    return ranges

def merge_ranges(ranges):
    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

def generate_invalid_ids(max_val):
    invalid = []
    max_len = len(str(max_val))
    for half_len in range(1, max_len // 2 + 1):
        start = 10**(half_len - 1)
        end = 10**half_len
        for half in range(start, end):
            n = int(str(half) * 2)
            if n > max_val:
                break
            invalid.append(n)
    return invalid

def sum_invalid_ids(ranges):
    merged = merge_ranges(ranges)
    max_val = max(r[1] for r in merged)

    invalid_ids = generate_invalid_ids(max_val)
    total = 0

    i = 0  
    m = len(merged)

    for n in invalid_ids:
        while i < m and n > merged[i][1]:
            i += 1
        if i == m:
            break
        if merged[i][0] <= n <= merged[i][1]:
            total += n

    return total

# ---- main ----
with open("input day 2.txt") as f:
    line = f.read().strip()

ranges = parse_ranges(line)
answer = sum_invalid_ids(ranges)
print(answer)
