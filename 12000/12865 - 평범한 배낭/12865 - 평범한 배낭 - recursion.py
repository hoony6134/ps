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
2
