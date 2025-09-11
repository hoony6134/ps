# BOJ 17219 - 비밀번호 찾기

def main():
    dic = {}
    N,M = map(int,input().split())
    for _ in range(N):
        a,b = input().split()
        dic[a] = b
    for _ in range(M):
        s = input()
        print(dic[s])
    
if __name__ == "__main__":
    main()
