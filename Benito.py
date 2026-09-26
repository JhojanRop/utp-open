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
        start_r, start_c = -1, -1

        for i in range(R):
            row = list(input_data[idx])
            idx += 1
            grid.append(row)
            if start_r == -1:
                for j in range(C):
                    if row[j] == "*":
                        start_r = i
                        start_c = j

        q = deque([(start_r, start_c)])
        grid[start_r][start_c] = "#"
        count = 0

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            r, c = q.popleft()
            count += 1

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == ".":
                    grid[nr][nc] = "#"
                    q.append((nr, nc))

        print(count)


if __name__ == "__main__":
    solve()
