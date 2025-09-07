# BOJ 16480 - 외심과 내심은 사랑입니다
import sys
input = sys.stdin.readline

def main():
    R, r = map(int,input().split())
    print(int(R**2-2*R*r))

if __name__ == "__main__":
    main()
