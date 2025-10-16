def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # print(K)
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    # print(K)
    return K[n][W]


def main():
    N, W = map(int, input().split())
    val = []
    wt = []
    for _ in range(N):
        a, b = map(int, input().split())
        wt.append(a)
        val.append(b)
    print(knapSack(W, wt, val, N))


if __name__ == "__main__":
    main()
