# BOJ 16489 - 삼각형 해커
from decimal import Decimal
import sys
input = sys.stdin.readline

def main():
    a, b, c = map(Decimal, input().split())
    s = (a + b + c) / Decimal('2')
    S = (s * (s - a) * (s - b) * (s - c)).sqrt()
    R = (a * b * c) / (Decimal('4') * S)
    r = S / s
    d_t = R ** 2 - Decimal('2') * R * r
    if d_t < 0:
        d_t = Decimal('0')
    d = d_t.sqrt()
    A = (b ** 2 + c ** 2 - a ** 2) / (Decimal('2') * b * c)
    B = (a ** 2 + c ** 2 - b ** 2) / (Decimal('2') * a * c)
    C = (a ** 2 + b ** 2 - c ** 2) / (Decimal('2') * a * b)
    k = R * (abs(A) + abs(B) + abs(C))
    print(f"{float(S):.13f}\n{float(R):.13f}\n{float(r):.13f}\n{float(d):.13f}\n{float(k):.13f}")

if __name__ == "__main__":
    main()
