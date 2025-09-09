# 26529. [Bunnies](https://www.acmicpc.net/problem/26529)

| 티어 | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
|---|---|---|---:|---:|---:|---:|
| <img src="https://static.solved.ac/tier_small/4.svg" width="20px" /> | 1 초 | 1024 MB | 958 | 721 | 668 | 75.480% |

---

## 문제

You’re going to raise farm animals and you decided to start with bunnies, the easiest of animals. To your surprise they are breeding like rabbits, so much so that you’re unable to count them accurately. However, you know that rabbits’ breeding patterns always follow the Fibonacci sequence. The Fibonacci sequence is defined as follows:

F(0) = 1, F(1) = 1, F(N) = F(N-1)+F(N-2)

Given the number of months the rabbits have been breeding, use the Fibonacci sequence to determine the number of rabbits you should have.

## 입력

The first line will contain a single integer n that indicates the number of data sets that follow. Each data set will start with a single integer x denoting the number of months that have passed since you bought your initial pair of rabbits. 0≤x≤45

## 출력

For each test case, output the expected number of rabbits after x months.

## 예제

### 예제 입력 1

```
3
0
5
45
```

### 예제 출력 1

```
1
8
1836311903
```

## 출처

School
\> 
PLU High School Programming Contest
\> 
PLU 2017
\> 
Novice
2번
School
\> 
PLU High School Programming Contest
\> 
PLU 2017
\> 
Advanced
2번

## 알고리즘 분류

- 수학
- 구현
- 다이나믹 프로그래밍

## 정답 코드

```python
# BOJ 26529 - Bunnies
import sys
input = sys.stdin.readline

# bottom-up
def rabbit(x):
    l = [0]*50
    l[0]=1
    l[1]=1
    for i in range(2,x+1):
        l[i] = l[i-1] + l[i-2]
    return l[x]

def main():
    n = int(input())
    for _ in range(n):
        k=int(input())
        print(rabbit(k))

if __name__ == "__main__":
    main()

```
