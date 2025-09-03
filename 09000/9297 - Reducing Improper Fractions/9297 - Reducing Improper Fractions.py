# BOJ 9297 - Reducing Improper Fractions
import sys
input = sys.stdin.readline

def main():
    cases = int(input())
    for i in range(cases):
        a,b = map(int, input().split())
        c = a//b
        d = a%b
        if c==0 and d==0:
            print("Case %d: 0" % (i+1))
        elif d == 0:
            print("Case %d: %d" % (i+1, c))
        elif c == 0:
            print("Case %d: %d/%d" % (i+1, d, b))
        else:
            print("Case %d: %d %d/%d" % (i+1, c, d, b))

if __name__ == "__main__":
    main()
