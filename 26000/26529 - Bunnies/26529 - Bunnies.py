# BOJ 26529 - Bunnies
import sys
input = sys.stdin.readline

# bottom-up
def rabbit(x):
    l = [0]*50
    l[0]=1
    l[1]=1
    for i in range(2,x+1):
        l[i] = l[i-1] + l[i-2]
    return l[x]

def main():
    n = int(input())
    for _ in range(n):
        k=int(input())
        print(rabbit(k))

if __name__ == "__main__":
    main()
