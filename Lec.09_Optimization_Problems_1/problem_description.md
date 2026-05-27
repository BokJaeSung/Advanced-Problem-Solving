# Lec.09 Optimization Problems (1) — Problem Descriptions

---

## PS.9.1 Longest Common Subsequence

### Description
두 개의 수열 X, Y가 주어졌을 때, 두 수열의 부분 수열이 되는 수열 중 가장 긴 공통 부분 수열 LCS(X, Y)를 찾으시오.

### Input
첫째 줄에 첫 번째 수열 X가 주어진다.  
둘째 줄에 두 번째 수열 Y가 주어진다.  
수열의 원소는 알파벳 문자로만 구성되어 있으며, 최대 100개의 문자로 이뤄져 있다.

### Output
첫째 줄에 두 수열의 가장 긴 공통 부분 수열의 길이를 출력한다.  
둘째 줄에 두 수열의 가장 긴 공통 부분 수열을 출력한다.  
가장 긴 공통 부분 수열은 여러 개 존재할 수 있으나, 강의자료에서 제시한 알고리즘의 출력을 출력해야 한다.

### Sample
```
Input:          Output:
ABCBDAB         4
BDCABA          BCBA
```

### Key Algorithm
- DP Tabulation
- dp[i][j] = X[1..i]와 Y[1..j]의 LCS 길이
- X[i] == Y[j] → dp[i-1][j-1] + 1 (DIAG)
- 아니면 max(dp[i-1][j], dp[i][j-1]) → UP 또는 LEFT
- path 테이블 역추적으로 LCS 복원
- T(n, m) = O(n × m)

---

## PS.9.2 Edit Distance

### Description
두 개의 문자열 X, Y가 주어졌을 때, X 문자열을 Y 문자열로 바꿀 수 있는 최소 편집 거리를 구하시오.

편집을 위한 명령은 아래와 같이 총 3가지가 있다.
- **추가(Insert)**: X 문자열에 한 글자를 추가한다.
- **삭제(Delete)**: X 문자열에서 한 글자를 삭제한다.
- **대체(Substitute)**: X 문자열의 한 글자를 다른 문자로 바꾼다.

### Input
첫째 줄에 문자열 X가 주어진다.  
둘째 줄에 문자열 Y가 주어진다.  
문자열은 알파벳 문자로만 구성되어 있으며, 최소 1개 최대 100개의 문자로 이뤄져 있다.

### Output
첫째 줄에 가장 짧은 편집 거리를 출력한다.  
둘째 줄에 가장 짧은 편집 거리로 X를 Y로 바꾸는 명령을 차례대로 출력한다.

명령 형식:
- `INSERT i c` : i번째 위치에 문자 c 추가
- `DELETE i c` : i번째 위치의 문자 c 삭제
- `SUBST i c` : i번째 위치의 문자를 c로 대체

### Sample
```
Input 1:        Output 1:         Input 2:      Output 2:
ABCBDAB         5                 fair          1
BDCABA          SUBST 1 B         fairy         INSERT 4 y
                SUBST 2 D
                SUBST 4 A
                SUBST 5 B
                DELETE 7 B
```

### Key Algorithm
- DP Tabulation
- dp[i][j] = X[1..i] → Y[1..j] 최소 편집 거리
- 세 연산 중 최솟값 선택 (동점: MATCH/SUBST > DEL > INS)
- path 테이블 역추적으로 명령 순서 복원
- T(n, m) = O(n × m)
