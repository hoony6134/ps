# BOJ 1049 - 기타줄
# Retry with some aid of GPT
import sys
input = sys.stdin.readline

def main():
    n,m=map(int,input().split())
    la = []
    lb = []
    for _ in range(m):
        ia,ib=map(int,input().split())
        la.append(ia); lb.append(ib)
    a = min(la); b = min(lb)
    price = min((n//6 + 1)*a,(n//6)*a+(n%6)*b,b*n)
    print(price)
        

if __name__ == "__main__":
    main()
