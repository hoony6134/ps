# BOJ 25600 - Triathlon
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    l = []
    for _ in range(n):
        a,d,g = map(int, input().split())
        s = a * (d + g)
        if a==(d+g):
            s *= 2
        l.append(s)
    print(max(l))

if __name__ == "__main__":
    main()
