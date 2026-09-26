import sys
import array

def main():

    if sys.stdin.isatty():
        print("Ingresa N en la primera línea, y luego los padres en la segunda línea:")

    input_stream = sys.stdin.buffer
    first_line = input_stream.readline()
    while first_line and not first_line.strip():
        first_line = input_stream.readline()

    if not first_line:
        return

    N = int(first_line)

    P = array.array('i', [0, 0])

    for line in input_stream:
        parts = line.split()
        if not parts:
            continue
        P.extend(map(int, parts))
        if len(P) >= N + 1:
            break

    if len(P) > N + 1:
        del P[N + 1:]

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
