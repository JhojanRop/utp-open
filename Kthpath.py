import sys
import heapq

def main():
    if sys.stdin.isatty():
        print("Ingresa N, M, K, S, D y luego las M aristas:")

    tokens = []
    total_needed = None

    for line in sys.stdin:
        for t in line.split():
            tokens.append(int(t))
            if total_needed is None and len(tokens) >= 5:
                total_needed = 5 + 3 * tokens[1]
            if total_needed is not None and len(tokens) >= total_needed:
                break
        if total_needed is not None and len(tokens) >= total_needed:
            break

    if not tokens or len(tokens) < 5:
        return

    N = tokens[0]
    M = tokens[1]
    K = tokens[2]
    S = tokens[3]
    D = tokens[4]

    adj = [[] for _ in range(N + 1)]
    idx = 5
    for e_idx in range(M):
        if idx + 2 >= len(tokens):
            break
        u = tokens[idx]
        v = tokens[idx + 1]
        w = tokens[idx + 2]
        idx += 3
        adj[u].append((v, w, e_idx))
        adj[v].append((u, w, e_idx))

    banned_edges = [False] * M

    def dijkstra():
        dist = [float('inf')] * (N + 1)
        dist[S] = 0
        parent = [0] * (N + 1)
        parent_edge = [-1] * (N + 1)
        pq = [(0, S)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == D:
                break
            for v, w, e_idx in adj[u]:
                if banned_edges[e_idx]:
                    continue
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    parent_edge[v] = e_idx
                    heapq.heappush(pq, (dist[v], v))

        if dist[D] == float('inf'):
            return None, None, None

        path = []
        path_edges = []
        curr = D
        while curr != 0:
            path.append(curr)
            if parent_edge[curr] != -1:
                path_edges.append(parent_edge[curr])
            curr = parent[curr]
        path.reverse()
        return dist[D], path, path_edges

    final_dist = None
    final_path = None

    for _ in range(K):
        d, path, p_edges = dijkstra()
        if path is None:
            break
        final_dist = d
        final_path = path
        for e in p_edges:
            banned_edges[e] = True

    if final_dist is not None and final_path is not None:
        print(final_dist)
        print(' - '.join(map(str, final_path)))

if __name__ == '__main__':
    main()
