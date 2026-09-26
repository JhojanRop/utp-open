import sys

def main():
    if sys.stdin.isatty():
        print("Ingresa los datos del problema:")

    tokens = []
    total_needed = None

    for line in sys.stdin:
        for t in line.split():
            tokens.append(t)
            if total_needed is None and len(tokens) >= 3:
                try:
                    n1 = int(tokens[2])
                    if len(tokens) >= 4 + n1:
                        n2 = int(tokens[3 + n1])
                        total_needed = 4 + n1 + n2
                except (ValueError, IndexError):
                    pass
            if total_needed is not None and len(tokens) >= total_needed:
                break
        if total_needed is not None and len(tokens) >= total_needed:
            break

    if not tokens or len(tokens) < 4:
        return

    K = int(tokens[0])
    T = int(tokens[1])

    N1 = int(tokens[2])
    idx = 3
    A1 = tokens[idx : idx + N1]
    idx += N1

    if idx >= len(tokens):
        return
    N2 = int(tokens[idx])
    idx += 1
    A2 = tokens[idx : idx + N2]

    dp = [[[-1, -1] for _ in range(K + 1)] for _ in range(T + 1)]
    dp[1][0][0] = 0

    for t in range(1, T):
        next_dp = [[[-1, -1] for _ in range(K + 1)] for _ in range(T + 1)]

        for p1 in range(1, t + 1):
            p2 = t - p1
            val1_last = A1[(p1 - 1) % N1]
            val2_last = A2[(p2 - 1) % N2] if p2 > 0 else None

            next_val1 = A1[p1 % N1]
            next_val2 = A2[p2 % N2]

            max_k = min(K, t - 1)
            for k in range(max_k + 1):
                s0 = dp[p1][k][0]
                if s0 != -1:
                    echo00 = 1 if next_val1 == val1_last else 0
                    if s0 + echo00 > next_dp[p1 + 1][k][0]:
                        next_dp[p1 + 1][k][0] = s0 + echo00
                    if k + 1 <= K:
                        echo01 = 1 if next_val2 == val1_last else 0
                        if s0 + echo01 > next_dp[p1][k + 1][1]:
                            next_dp[p1][k + 1][1] = s0 + echo01

                s1 = dp[p1][k][1]
                if s1 != -1:
                    if k + 1 <= K:
                        echo10 = 1 if next_val1 == val2_last else 0
                        if s1 + echo10 > next_dp[p1 + 1][k + 1][0]:
                            next_dp[p1 + 1][k + 1][0] = s1 + echo10

                    echo11 = 1 if next_val2 == val2_last else 0
                    if s1 + echo11 > next_dp[p1][k][1]:
                        next_dp[p1][k][1] = s1 + echo11

        dp = next_dp

    ans = 0
    for p1 in range(1, T + 1):
        for k in range(K + 1):
            if dp[p1][k][0] > ans:
                ans = dp[p1][k][0]
            if dp[p1][k][1] > ans:
                ans = dp[p1][k][1]

    print(ans)

if __name__ == '__main__':
    main()
