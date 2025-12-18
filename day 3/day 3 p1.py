total = 0

with open("input day 3.txt") as f:
    for line in f:
        s = line.strip()
        if not s:
            continue

        best = 0
        n = len(s)

        for i in range(n):
            d1 = int(s[i])
            for j in range(i + 1, n):
                val = d1 * 10 + int(s[j])
                if val > best:
                    best = val

        total += best

print(total)
