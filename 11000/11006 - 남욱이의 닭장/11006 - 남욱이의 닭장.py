# BOJ 11006 - 남욱이의 닭장
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = m * 2 - n
    print(l, m - l)
