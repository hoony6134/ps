
def bubble_sort(li):
    for i in range(len(li)-1):
        if li[i] >= li[i+1]:
            t = li[i]
            li[i] = li[i+1]
            li[i+1] = t
    return li

def main():
    n = int(input())
    li = []
    for _ in range(n):
        li.append(int(input()))
    print(bubble_sort(li))
    
if __name__ == "__main__":
    main()
