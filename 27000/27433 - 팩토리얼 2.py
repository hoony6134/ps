# BOJ 27433 - 팩토리얼 2
import sys

def main():
    n = int(input())
    r = 1
    for i in range(1,n+1):
        r *= i
    print(r)
        

if __name__ == "__main__":
    main()
