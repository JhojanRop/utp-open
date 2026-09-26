import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        R = int(input_data[idx])
        C = int(input_data[idx + 1])
        idx += 2

        if R == 0 and C == 0:
            break

        grid = []
        start_r = -1
        start_c = -1

        for i in range(R):
            row = input_data[idx]
            idx += 1
            grid.append(row)
            if "*" in row:
                start_r = i
                start_c = row.index("*")

        visited = [[False] * C for _ in range(R)]
        visited[start_r][start_c] = True

        queue = deque([(start_r, start_c)])
        count = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()
            count += 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < R and 0 <= nc < C:  # noqa: SIM102
                    if not visited[nr][nc] and grid[nr][nc] == ".":
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        print(count)


if __name__ == "__main__":
    solve()
