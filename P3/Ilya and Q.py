import sys

def count_pairs(s):
    n = len(s)
    pairs_count = [0] * n

    for i in range(1, n):
        if s[i] == s[i - 1]:
            pairs_count[i] = pairs_count[i - 1] + 1
        else:
            pairs_count[i] = pairs_count[i - 1]
        print(pairs_count)
    return pairs_count

def main():
    resultado_final = []
    s = sys.stdin.readline()
    m = int(sys.stdin.readline())
    pairs_count = count_pairs(s)

    for _ in range(m):
        linea = sys.stdin.readline()
        li, ri = map(int, linea.split())
        result = pairs_count[ri - 1] - pairs_count[li - 1]
        resultado_final.append(result)

    for i in resultado_final:
        sys.stdout.write(str(i)+"\n")
if __name__ == "__main__":
    main()
