import sys
import array

def main():
    input_stream = sys.stdin.buffer

    if sys.stdin.isatty():
        print("Ingresa N y luego los N-1 padres (se procesa al completar los datos):")

    CHUNK_SIZE = 1024 * 1024
    rem = b''
    N = None
    P = array.array('i', [0, 0])

    while True:
        chunk = input_stream.read(CHUNK_SIZE)
        if not chunk:
            if rem:
                for token in rem.split():
                    val = int(token)
                    if N is None:
                        N = val
                    else:
                        P.append(val)
            break

        data = rem + chunk
        last_ws = max(data.rfind(b' '), data.rfind(b'\n'), data.rfind(b'\r'), data.rfind(b'\t'))
        if last_ws == -1:
            rem = data
            continue

        rem = data[last_ws + 1:]
        tokens = data[:last_ws].split()
        if not tokens:
            continue

        idx = 0
        if N is None:
            N = int(tokens[0])
            idx = 1

        P.extend(map(int, tokens[idx:]))
        if len(P) >= N + 1:
            break

    if N is None or N < 2:
        return

    if len(P) > N + 1:
        del P[N + 1:]
    elif len(P) < N + 1:
        if sys.stdin.isatty():
            print(f"Error: se esperaban {N - 1} padres para N = {N}, pero solo se recibieron {len(P) - 2}.", file=sys.stderr)
        return

    sz = array.array('i', [1]) * (N + 1)
    h1 = array.array('i', [-1]) * (N + 1)
    h2 = array.array('i', [-1]) * (N + 1)
    F  = array.array('i', [0]) * (N + 1)

    total_dist = 0

    for i in range(N, 1, -1):
        p = P[i]
        sz_i = sz[i]
        sz[p] += sz_i
        total_dist += sz_i * (N - sz_i)

        h1_i = h1[i]
        h2_i = h2[i]

        if h1_i == -1:
            H_i = 0
            path_i = 0
        elif h2_i == -1:
            H_i = h1_i + 1
            path_i = H_i
        else:
            H_i = h1_i + 1
            path_i = h1_i + h2_i + 2

        if path_i > F[i]:
            F[i] = path_i

        F_i = F[i]
        if F_i > F[p]:
            F[p] = F_i

        if H_i >= h1[p]:
            h2[p] = h1[p]
            h1[p] = H_i
        elif H_i > h2[p]:
            h2[p] = H_i

    h1_1 = h1[1]
    h2_1 = h2[1]
    if h1_1 == -1:
        path_1 = 0
    elif h2_1 == -1:
        path_1 = h1_1 + 1
    else:
        path_1 = h1_1 + h2_1 + 2

    if path_1 > F[1]:
        F[1] = path_1

    out = sys.stdout.buffer
    out.write(str(total_dist).encode('ascii') + b'\n')

    OUT_CHUNK = 50000
    for i in range(1, N + 1, OUT_CHUNK):
        end = min(i + OUT_CHUNK, N + 1)
        chunk_str = ' '.join(map(str, F[i:end]))
        chunk_str += ' ' if end <= N else '\n'
        out.write(chunk_str.encode('ascii'))

if __name__ == '__main__':
    main()
