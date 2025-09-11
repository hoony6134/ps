# 26173. [Cup Covering](https://www.acmicpc.net/problem/26173)

| 티어 | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
|---|---|---|---:|---:|---:|---:|
| <img src="https://static.solved.ac/tier_small/4.svg" width="20px" /> | 1 초 (추가 시간 없음) | 1024 MB | 171 | 137 | 107 | 90.678% |

---

## 문제

Janneke is addicted to Dutch stroopwafels. She could eat them the whole day, every day. What she loves most during the colder seasons, is to put a stroopwafel on top of a cup full of hot, steaming cocoa. This way, the stroopwafel warms and softens and the caramel melts, leaving a gooey but delicious mess between her fingers when she picks it up.

For \name, this is pure heaven. Or well, it could be if she could just find the perfect cup for the round stroopwafels. Instead, she is left with unsatisfying stroopwafel experiences time and time again. Either the opening of the cup is too small for her stroopwafel and the edges stay hard and cold or -- even worse -- the opening is too large and the stroopwafel just falls in with a splash, becoming soggy and disgusting.

Janneke finally has had enough and decides to take matters into her own hands. She establishes the  *Ideal Cup Production Company*  (ICPC) which produces the ideal stroopwafel cups. Customers can simply tell her the area of the round stroopwafel they prefer and she delivers a cup with an opening that is perfectly covered by the stroopwafel. For the production, she needs to determine the diameter of the cup opening first. Soon, she will have orders from all over the world which she can barely keep up with, so she might need a little help here.

## 입력

The input consists of:

- One line with an integer $a$ ($0 < a\leq $10^{15}$$), the area of the round stroopwafel in $\text{cm}^2$.

## 출력

Output the diameter of the ideal cup in centimetres such that a stroopwafel with area $a$ covers it perfectly. Note that the rim of the cup is so thin that it can be neglected.

Your answer should have an absolute or relative error of at most $$10^{-9}$$.

## 예제

### 예제 입력 1

```
42
```

### 예제 출력 1

```
7.3127327914
```

## 예제

### 예제 입력 2

```
20221126
```

### 예제 출력 2

```
5074.0848694393
```

## 출처

![image](https://licensebuttons.net/l/by-sa/4.0/88x31.png)

ICPC
\> 
Regionals
\> 
Europe
\> 
Northwestern European Regional Contest
\> 
NWERC 2022 연습 세션
PC번

- 문제를 만든 사람: The NWERC 2022 Jury

## 알고리즘 분류

- 수학
- 기하학
- 사칙연산

## 정답 코드

```python
# BOJ 26173 - Cup Covering
import sys
import math
input = sys.stdin.readline

def main():
    a = int(input())
    print(f"{float(2*math.sqrt(a/math.pi)):.10f}")

if __name__ == "__main__":
    main()

```
