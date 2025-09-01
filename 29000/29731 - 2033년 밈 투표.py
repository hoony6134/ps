# BOJ 29731 - 2033년 밈 투표
import sys

def main():
    l = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]
    n = int(input())
    for _ in range(n):
        if input() in l:
            continue
        else:
            print("Yes")
            sys.exit(0)
    print("No")

if __name__ == "__main__":
    main()
