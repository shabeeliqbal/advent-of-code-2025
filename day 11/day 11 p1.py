import sys

def read_graph(fn="input.txt"):
    g = {}
    with open(fn) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, rest = line.split(":")
            name = name.strip()
            targets = [t for t in rest.strip().split() if t]
            g[name] = targets
    return g

def count_paths(graph, start="you", target="out"):
    memo = {}
    visiting = set()

    def dfs(u):
        if u == target:
            return 1
        if u in memo:
            return memo[u]
        if u in visiting:
            raise RuntimeError(f"cycle detected at {u}")
        visiting.add(u)
        total = 0
        for v in graph.get(u, []):
            total += dfs(v)
        visiting.remove(u)
        memo[u] = total
        return total

    return dfs(start)

if __name__ == "__main__":
    graph = read_graph("input day 11.txt")
    print(count_paths(graph, "you", "out"))
