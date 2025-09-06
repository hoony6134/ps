# BOJ 2748 - 피보나치 수 2
import sys
input = sys.stdin.readline

global dp
dp = [0]*100

def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

def main():
    a = int(input())
    print(fibo(a))

if __name__ == "__main__":
    main()
