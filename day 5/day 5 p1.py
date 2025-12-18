def parse_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]

    split_idx = lines.index('')
    range_lines = lines[0:split_idx]
    id_lines = lines[split_idx+1:]

    ranges = []
    for line in range_lines:
        if not line:
            continue
        a, b = line.split('-')
        ranges.append((int(a), int(b)))

    ids = [int(x) for x in id_lines if x]
    return ranges, ids

def merge_ranges(ranges):
    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

def count_fresh_ids(ranges, ids):
    merged = merge_ranges(ranges)
    fresh_count = 0

    for id_val in ids:
        for start, end in merged:
            if id_val < start:
                break
            if start <= id_val <= end:
                fresh_count += 1
                break

    return fresh_count

# ---- main ----
ranges, ids = parse_input("input day 5.txt")
answer = count_fresh_ids(ranges, ids)
print(answer)
