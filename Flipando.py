import heapq
import sys


class Node:
    __slots__ = ["idx", "p", "w"]

    def __init__(self, w, p, idx):
        self.w = w
        self.p = p
        self.idx = idx

    def __lt__(self, other):
        return self.w * other.p > other.w * self.p


def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)

    token_iter = get_ints()

    try:
        n = next(token_iter)
    except StopIteration:
        return

    P = [0] * (n + 1)
    W = [0] * (n + 1)
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        P[i] = next(token_iter)

    for i in range(1, n + 1):
        W[i] = next(token_iter)

    m = next(token_iter)

    for _ in range(m):
        u = next(token_iter)
        v = next(token_iter)
        parent[u] = v

    dsu = list(range(n + 1))

    def find(i):
        root = i
        while dsu[root] != root:
            root = dsu[root]
        curr = i
        while curr != root:
            nxt = dsu[curr]
            dsu[curr] = root
            curr = nxt
        return root

    ans = 0
    for i in range(1, n + 1):
        ans += P[i] * W[i]

    pq = []
    for i in range(1, n + 1):
        heapq.heappush(pq, Node(W[i], P[i], i))

    while pq:
        item = heapq.heappop(pq)
        v = item.idx

        if dsu[v] != v:
            continue

        if item.w != W[v] or item.p != P[v]:
            continue

        u = find(parent[v])

        ans += P[u] * W[v]
        P[u] += P[v]
        W[u] += W[v]
        dsu[v] = u

        if u != 0:
            heapq.heappush(pq, Node(W[u], P[u], u))

    print(ans)


if __name__ == "__main__":
    solve()
