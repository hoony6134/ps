# BOJ 25192 - 인사성 밝은 곰곰이

def main():
    n = int(input())
    i = 0
    s = set()
    c = 0
    while True:
        i+=1
        if i==n+1:
            break
        else:
            a = input()
            if a=="ENTER":
                c += len(s)
                s.clear()
            else:
                s.add(a)
    c += len(s)
    print(c)        

if __name__ == "__main__":
    main()
