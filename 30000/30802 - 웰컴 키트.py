# BOJ 30802 - 웰컴 키트
import sys

def main():
    n = int(input())
    s,m,l,xl,xxl,xxxl = map(int, input().split())
    t,p = map(int, input().split())
    z = 0
    z += s//t + (s%t!=0)
    z += m//t + (m%t!=0)
    z += l//t + (l%t!=0)
    z += xl//t + (xl%t!=0)
    z += xxl//t + (xxl%t!=0)
    z += xxxl//t + (xxxl%t!=0)
    print(z)
    print(n//p,n%p)

if __name__ == "__main__":
    main()
