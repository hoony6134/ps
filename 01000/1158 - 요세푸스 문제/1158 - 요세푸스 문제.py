# BOJ 1158 - 요세푸스 문제
from collections import deque


def play(n, k):
    q = deque(range(1, n + 1))
    list = []
    while q:
        q.rotate(-(k - 1))
        list.append(q.popleft())
    print("<", end="")
    print(*list, sep=", ", end="")
    print(">")


n, k = map(int, input().split())
play(n, k)
