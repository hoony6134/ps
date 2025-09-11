# BOJ 1003 - 피보나치 함수
# debugged and improved with GPT
import sys
input = sys.stdin.readline

global dp, cz, co
dp = [None] * 50

def fibo(n):
    global dp
    if n==0:
        return (1, 0)
    elif n==1:
        return (0, 1)
    elif dp[n] != None:
        return dp[n]
    a0, a1 = fibo(n-1)
    b0, b1 = fibo(n-2)
    dp[n] = (a0+b0, a1+b1)
    return dp[n]

def main():
    global dp
    n = int(input())
    for _ in range(n):
        a = int(input())
        z,o = fibo(a)
        print(z,o)
        dp = [None] * 50

if __name__ == "__main__":
    main()
