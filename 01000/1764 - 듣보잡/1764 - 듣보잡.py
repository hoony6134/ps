# BOJ 1764 - 듣보잡
import sys

def main():
    dn = set()
    bn = set()
    n, m = map(int,input().split())
    for _ in range(n):
        dn.add(input())
    for _ in range(m):
        bn.add(input())
    print(len(dn.intersection(bn)))
    for i in sorted(dn.intersection(bn)):
        print(i)

if __name__ == "__main__":
    main()
