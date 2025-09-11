# BOJ 26173 - Cup Covering
import sys
import math
input = sys.stdin.readline

def main():
    a = int(input())
    print(f"{float(2*math.sqrt(a/math.pi)):.10f}")

if __name__ == "__main__":
    main()
