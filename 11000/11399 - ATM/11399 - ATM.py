# BOJ 11399 - ATM

def main():
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    
    l.sort()
    for i in range(1,n+1):
        c += (n-(i-1))*l[i-1]
    print(c)

if __name__ == "__main__":
    main()
