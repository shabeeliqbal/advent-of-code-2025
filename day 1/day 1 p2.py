position = 50
count_zero = 0

with open("input day 1.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])
        step = 1 if direction == "R" else -1

        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                count_zero += 1

print(count_zero)
