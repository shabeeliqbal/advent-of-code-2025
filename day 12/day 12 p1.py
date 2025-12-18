from os import environ
import sys

sys.setrecursionlimit(20000)

def parse_input(lines):
    shapes, grids, current_id = {}, [], -1
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "x" in line and ":" in line:
            dims, counts = line.split(":")
            grids.append((*map(int, dims.split("x")), list(map(int, counts.split()))))
        elif line.endswith(":"):
            current_id = int(line[:-1])
            shapes[current_id] = []
        else:
            val = sum((c == "#") << (len(line) - 1 - i) for i, c in enumerate(line))
            shapes[current_id].append((val, len(line)))
    return shapes, grids

def generate_variations(base_shapes):
    variations = {}
    for sid, rows in base_shapes.items():
        max_w = max(r[1] for r in rows)
        matrix = []
        for val, w in rows:
            matrix.append([(val >> (w - 1 - i)) & 1 for i in range(max_w)])
        seen = set()
        shape_vars = []
        current = matrix
        for _ in range(2):
            for _ in range(4):
                min_r, max_r = len(current), -1
                min_c, max_c = len(current[0]), -1
                has_bits = False
                for r in range(len(current)):
                    for c in range(len(current[0])):
                        if current[r][c]:
                            has_bits = True
                            min_r, max_r = min(min_r, r), max(max_r, r)
                            min_c, max_c = min(min_c, c), max(max_c, c)
                if has_bits:
                    h = max_r - min_r + 1
                    w = max_c - min_c + 1
                    rows_int = []
                    for r in range(min_r, max_r + 1):
                        v = 0
                        for c in range(min_c, max_c + 1):
                            v = (v << 1) | current[r][c]
                        rows_int.append(v)
                    sig = tuple(rows_int)
                    if sig not in seen:
                        seen.add(sig)
                        shape_vars.append((h, w, rows_int))
                h, w = len(current), len(current[0])
                current = [[current[h - 1 - r][c] for r in range(h)] for c in range(w)]
            current = current[::-1]
        shape_vars.sort(key=lambda x: -x[0])
        variations[sid] = shape_vars
    return variations

def is_space_sufficient(grid, width, height, required_area, min_item_area, slack=20):
    used = sum(bin(r).count("1") for r in grid)
    free = width * height - used
    if free < required_area:
        return False
    if free > required_area + slack:
        return True
    occupied = set()
    for r in range(height):
        for c in range(width):
            if (grid[r] >> (width - 1 - c)) & 1:
                occupied.add((r, c))
    visited = set()
    usable = 0
    for r in range(height):
        for c in range(width):
            if (r, c) in occupied or (r, c) in visited:
                continue
            stack = [(r, c)]
            visited.add((r, c))
            size = 0
            while stack:
                x, y = stack.pop()
                size += 1
                for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if 0 <= nx < height and 0 <= ny < width:
                        if (nx, ny) not in occupied and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            stack.append((nx, ny))
            if size >= min_item_area:
                usable += size
            if usable >= required_area:
                return True
    return usable >= required_area

def solve_recursive(grid, items, idx, width, height, variations, min_area):
    if idx == len(items):
        return True
    need = sum(it["area"] for it in items[idx:])
    if not is_space_sufficient(grid, width, height, need, min_area):
        return False
    item = items[idx]
    sid = item["id"]
    sr, sc = 0, 0
    if idx > 0 and items[idx-1]["id"] == sid:
        sr, sc = items[idx-1]["placed_r"], items[idx-1]["placed_c"]
    for h, w, rows in variations[sid]:
        for r in range(sr, height - h + 1):
            cb = sc if r == sr else 0
            for c in range(cb, width - w + 1):
                shift = width - c - w
                if all(not (grid[r+i] & (rows[i] << shift)) for i in range(h)):
                    for i in range(h):
                        grid[r+i] |= rows[i] << shift
                    item["placed_r"], item["placed_c"] = r, c
                    if solve_recursive(grid, items, idx+1, width, height, variations, min_area):
                        return True
                    for i in range(h):
                        grid[r+i] ^= rows[i] << shift
    return False

def part1(lines):
    shapes, regions = parse_input(lines)
    variations = generate_variations(shapes)
    areas = {sid: sum(bin(r).count("1") for r in vars[0][2]) for sid, vars in variations.items()}
    valid = 0
    for w, h, counts in regions:
        items = []
        for sid, cnt in enumerate(counts):
            for _ in range(cnt):
                items.append({"id": sid, "area": areas[sid], "placed_r": 0, "placed_c": 0})
        if not items:
            valid += 1
            continue
        items.sort(key=lambda x: (-x["area"], x["id"]))
        if sum(i["area"] for i in items) > w * h:
            continue
        grid = [0] * h
        if solve_recursive(grid, items, 0, w, h, variations, items[-1]["area"]):
            valid += 1
    return valid

if __name__ == "__main__":
    print(part1(open("input day 12.txt").read().splitlines()))
