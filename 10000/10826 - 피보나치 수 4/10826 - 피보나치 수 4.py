# BOJ 10826 - 피보나치 수 4
import sys
input = sys.stdin.readline


global l
l = [None] * 10001

def fib(n):
    if n<=1:
        l[n]=n
    if l[n] is None:
        l[n] = fib(n-1) + fib(n-2)
    return l[n]
    

def main():
    sys.setrecursionlimit(20000)
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
