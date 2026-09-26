import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    out = []

    while idx < len(input_data):
        R = int(input_data[idx])
        C = int(input_data[idx + 1])
        idx += 2

        if R == 0 and C == 0:
            break

        grid_chars = "".join(input_data[idx : idx + R])
        idx += R

        grid = bytearray(grid_chars, "ascii")
        start_pos = grid.find(b"*")

        stack = [start_pos]
        grid[start_pos] = 35
        count = 0

        while stack:
            pos = stack.pop()
            count += 1

            r = pos // C
            c = pos % C

            if r > 0:
                npos = pos - C
                if grid[npos] == 46:
                    grid[npos] = 35
                    stack.append(npos)
            if r < R - 1:
                npos = pos + C
                if grid[npos] == 46:
                    grid[npos] = 35
                    stack.append(npos)
            if c > 0:
                npos = pos - 1
                if grid[npos] == 46:
                    grid[npos] = 35
                    stack.append(npos)
            if c < C - 1:
                npos = pos + 1
                if grid[npos] == 46:
                    grid[npos] = 35
                    stack.append(npos)

        out.append(str(count))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()
