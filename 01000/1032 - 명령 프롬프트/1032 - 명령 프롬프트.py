# BOJ 1032 - 명령 프롬프트
import sys

def main():
    n = int(input())
    l = []
    result = ""
    for _ in range(n):
        l.append(input())
    for i in range(len(l[0])):
        tmp = l[0][i]
        verdict = 1
        for j in range(n):
            if l[j][i] != tmp:
                verdict = 0
                break
            else:
                continue
        if verdict:
            result = result + tmp
        else:
            result = result + '?'
    print(result)
                

if __name__ == "__main__":
    main()
