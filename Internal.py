import sys

def main():
    if sys.stdin.isatty():
        print("Ingresa q y luego los q valores de n:")

    tokens = []
    q = None

    for line in sys.stdin:
        for t in line.split():
            tokens.append(int(t))
            if q is None and len(tokens) >= 1:
                q = tokens[0]
            if q is not None and len(tokens) >= 1 + q:
                break
        if q is not None and len(tokens) >= 1 + q:
            break

    if not tokens or q is None or q < 1:
        return

    MOD = 10**9 + 7
    INV6 = 166666668

    results = []
    for i in range(1, 1 + q):
        if i >= len(tokens):
            break
        n = tokens[i]
        ans = (n % MOD * ((n - 1) % MOD) % MOD * ((n - 2) % MOD) % MOD * INV6) % MOD
        results.append(str(ans))

    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    main()
