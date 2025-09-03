# BOJ 11557 - Yangjojang of The Year
import sys

def main():
    n = int(input())
    l = []
    temp_max = -1
    for _ in range(n):
        m = int(input())
        for _ in range(m):
            school, num = map(str,input().split())
            num = int(num)
            l.append([school, num])
        for i in range(len(l)):
            if (l[i][1] >= temp_max):
                target_school = l[i][0]
                temp_max = l[i][1]
        print(target_school)

if __name__ == "__main__":
    main()
