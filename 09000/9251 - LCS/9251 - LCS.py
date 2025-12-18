# BOJ 9251 - LCS
import sys

input = sys.stdin.readlines
sys.setrecursionlimit(1000000)


def lcs(X, Y):
    n = len(X)
    m = len(Y)
    L = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = 1 + L[i - 1][j - 1]
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[n][m]


def lcs_mem(X, Y, i, j, L):
    if i == 0 or j == 0:
        return 0
    elif L[i][j] != -1:
        return L[i][j]
    elif X[i - 1] == Y[j - 1]:
        L[i][j] = 1 + lcs_mem(X, Y, i - 1, j - 1, L)
    else:
        L[i][j] = max(lcs_mem(X, Y, i - 1, j, L), lcs_mem(X, Y, i, j - 1, L))
    return L[i][j]


def main():
    a, b = map(str, input())
    a = a.strip()
    b = b.strip()

    L = [[-1] * (len(b) + 1) for _ in range(len(a) + 1)]
    print(lcs_mem(a, b, len(a), len(b), L))
    # print(lcs(a.strip(), b.strip()))


if __name__ == "__main__":
    main()
