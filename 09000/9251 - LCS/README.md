# 9251. [LCS](https://www.acmicpc.net/problem/9251)

| 티어 | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
|---|---|---|---:|---:|---:|---:|
| <img src="https://static.solved.ac/tier_small/11.svg" width="20px" /> | 0.1 초  (하단 참고) | 256 MB | 112048 | 48475 | 35489 | 42.455% |

---

## 문제

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

## 입력

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

## 출력

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

## 예제

### 예제 입력 1

```
ACAYKP
CAPCAK
```

### 예제 출력 1

```
4
```

## 출처

- 문제를 만든 사람: baekjoon
- 데이터를 추가한 사람: bang627 , beginnertomaster , eric00513 , fs_edge , qpwoeiruty

## 시간 제한

- Java 8: 0.4 초
- Python 3: 2 초
- PyPy3: 2 초
- Java 8 (OpenJDK): 0.4 초
- Java 11: 0.4 초
- Kotlin (JVM): 0.4 초
- Java 15: 0.4 초

## 알고리즘 분류

- 다이나믹 프로그래밍
- 문자열
- 최장 공통 부분 수열 문제

## 정답 코드

```python
# BOJ 9251 - LCS
import sys

input = sys.stdin.readlines
sys.setrecursionlimit(1000000)


def lcs(X, Y):
    n = len(X)
    m = len(Y)
    L = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = 1 + L[i - 1][j - 1]
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[n][m]


def lcs_mem(X, Y, i, j, L):
    if i == 0 or j == 0:
        return 0
    elif L[i][j] != -1:
        return L[i][j]
    elif X[i - 1] == Y[j - 1]:
        L[i][j] = 1 + lcs_mem(X, Y, i - 1, j - 1, L)
    else:
        L[i][j] = max(lcs_mem(X, Y, i - 1, j, L), lcs_mem(X, Y, i, j - 1, L))
    return L[i][j]


def main():
    a, b = map(str, input())
    a = a.strip()
    b = b.strip()

    L = [[-1] * (len(b) + 1) for _ in range(len(a) + 1)]
    print(lcs_mem(a, b, len(a), len(b), L))
    # print(lcs(a.strip(), b.strip()))


if __name__ == "__main__":
    main()

```
