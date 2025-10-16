def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # print(K)
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:  # 양쪽 첫줄 0으로
                K[i][w] = 0
            elif wt[i - 1] <= w:  # 이전거 무게가 해당 가방의 무게 제한보다 작으면
                K[i][w] = max(
                    val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]
                )  # 이전거 가치 + 무게 제한에서 이전거 무게를 뺀 것의 가치 / 이전거 가치 중 큰 것
            else:
                K[i][w] = K[i - 1][w]  # 이전걸 현재 가치로 채택
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
