def parse_ranges(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]

    split_idx = lines.index('')
    range_lines = lines[:split_idx]

    ranges = []
    for line in range_lines:
        if not line:
            continue
        a, b = line.split('-')
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

def count_fresh_ids_from_ranges(ranges):
    merged = merge_ranges(ranges)
    total = 0
    for start, end in merged:
        total += end - start + 1
    return total

# ---- main ----
ranges = parse_ranges("input day 5.txt")
answer = count_fresh_ids_from_ranges(ranges)
print(answer)
