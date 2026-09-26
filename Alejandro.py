import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])

    c = 0
    counts = [0] * 26

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    ord_a = 97

    decrypted_words = []

    for word in input_data[2:2 + N]:
        chars = []
        for ch in word:
            val_C = ord(ch) - ord_a

            val_L = (val_C - c) % 26

            counts[val_L] += 1

            if counts[val_L] % K == 0:
                c = (c + 1) % 26

            chars.append(ALPHABET[val_L])

        decrypted_words.append("".join(chars))

    sys.stdout.write(" ".join(decrypted_words) + "\n")

if __name__ == '__main__':
    main()
