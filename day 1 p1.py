position = 50
count_zero = 0

with open("input day 1.txt") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        value = int(line[1:])

        if direction == "L":
            position = (position - value) % 100
        else:
            position = (position + value) % 100

        if position == 0:
            count_zero += 1

print(count_zero)
