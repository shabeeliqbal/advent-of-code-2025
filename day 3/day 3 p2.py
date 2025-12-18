k = 12 
total = 0

with open("input day 3.txt") as f:
    for line in f:
        s = line.strip()
        if not s:
            continue

        n = len(s)
        remove = n - k
        stack = []

        for ch in s:
            while remove > 0 and stack and stack[-1] < ch:
                stack.pop()
                remove -= 1
            stack.append(ch)

        if remove > 0:
            stack = stack[:-remove]

        best_str = "".join(stack[:k])
        total += int(best_str)

print(total)
