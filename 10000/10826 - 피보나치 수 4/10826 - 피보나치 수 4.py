# BOJ 10826 - 피보나치 수 4
import sys
input = sys.stdin.readline


global l
l = [None] * 10001

# top-down
def fib(n):
    if n<=1:
        l[n]=n
    if l[n] is None:
        l[n] = fib(n-1) + fib(n-2)
    return l[n]

# bottom-up
def fib_bu(n):
    if n==0:
        return 0
    li = [0] * (n+1)
    li[1] = 1
    for i in range(2,n+1):
        li[i] = li[i-1] + li[i-2]
    return li[n]
    
def main():
    sys.setrecursionlimit(20000)
    n = int(input())
    print(fib_bu(n))

if __name__ == "__main__":
    main()
