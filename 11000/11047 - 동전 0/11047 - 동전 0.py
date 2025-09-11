# BOJ 11047 - 동전 0
import sys
input = sys.stdin.readline

def main():
    n,k=map(int,input().split())
    l = []
    cnt = 0
    for _ in range(n):
        l.append(int(input()))
    l.reverse()
    for i in range(len(l)):
        if k<l[i]:
            continue
        else:
            cnt += k//l[i]
            k -= (k//l[i])*l[i]
    print(cnt)

if __name__ == "__main__":
    main()
