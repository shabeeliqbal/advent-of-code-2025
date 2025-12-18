from math import inf

def read_points(filename="input day 8.txt"):
    points = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))
    return points

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def main():
    points = read_points("input day 8.txt")
    n = len(points)

    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx*dx + dy*dy + dz*dz
            edges.append((d2, i, j))

    edges.sort(key=lambda e: e[0])

    dsu = DSU(n)
    components = n
    last_pair = None

    for _, a, b in edges:
        if dsu.union(a, b):
            components -= 1
            last_pair = (a, b)
            if components == 1:
                break

    if last_pair is None:
        print("No connection made")
        return

    a, b = last_pair
    x1 = points[a][0]
    x2 = points[b][0]
    print(x1 * x2)

if __name__ == "__main__":
    main()
