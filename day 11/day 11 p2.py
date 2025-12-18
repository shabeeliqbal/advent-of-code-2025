import sys

def read_graph(fn="input.txt"):
    g = {}
    with open(fn) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, rest = line.split(":", 1)
            name = name.strip()
            targets = [t for t in rest.strip().split() if t]
            g[name] = targets
    return g

def count_paths_with_both(graph, start="svr", target="out", a="dac", b="fft"):
    memo = {}
    visiting = set()

    def dfs(u, saw_a, saw_b):
        key = (u, saw_a, saw_b)
        if key in memo:
            return memo[key]
        if u in visiting:
            raise RuntimeError("cycle detected reachable from start; infinite paths possible")
        if u == target:
            return 1 if (saw_a and saw_b) else 0

        visiting.add(u)
        total = 0
        for v in graph.get(u, []):
            total += dfs(v, saw_a or (v == a), saw_b or (v == b))
        visiting.remove(u)
        memo[key] = total
        return total
    
    return dfs(start, start == a, start == b)

if __name__ == "__main__":
    graph = read_graph("input day 11.txt")
    print(count_paths_with_both(graph, start="svr", target="out", a="dac", b="fft"))
