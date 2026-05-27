# Lec.04 String Matching — Problem Descriptions

---

## PS.4.1 String Pattern Matching

### Description
문자열 T와 패턴 P가 주어질 때, T에서 P가 등장하는 모든 위치(shift)를 출력하시오.

### Input
첫째 줄에 텍스트 문자열 T가 주어진다.  
둘째 줄에 패턴 문자열 P가 주어진다.

### Output
첫째 줄에 P가 등장하는 횟수를 출력한다.  
패턴이 등장하는 경우, 둘째 줄에 등장하는 위치(0-indexed shift)를 공백으로 구분하여 출력한다.

### Key Algorithm
- KMP (Knuth-Morris-Pratt)
- π (failure function) 테이블로 불필요한 비교 제거
- T(n, m) = O(n + m)

---

## PS.4.2 String Exponentiation

### Description
문자열 S가 주어졌을 때, S가 어떤 문자열 W를 k번 반복한 형태인 W^k 라면 최대 k를 출력하시오.  
반복 문자열이 없으면 1을 출력한다.

### Input
첫째 줄에 테스트 케이스의 수 n이 주어진다.  
이후 n개의 줄에 한 줄에 하나씩 문자열 S가 주어진다.

### Output
각 문자열에 대해 최대 지수 k를 한 줄에 하나씩 출력한다.

### Key Algorithm
- KMP π 테이블 활용
- period = n - π[n-1]
- n % period == 0 이면 k = n // period, 아니면 k = 1
- T(n) = O(n)

---

## PS.4.3 Longest Repeated Substring

### Description
문자열 S가 주어졌을 때, S에서 두 번 이상 등장하는 부분 문자열 중 가장 긴 것의 길이를 출력하시오.

### Input
문자열 S가 주어진다.

### Output
가장 긴 반복 부분 문자열의 길이를 출력한다.  
반복 부분 문자열이 없으면 0을 출력한다.

### Key Algorithm
- 이진 탐색 + Rabin-Karp 해싱
- 길이 L에 대해 중복 substring 존재 여부를 O(n)에 확인
- T(n) = O(n log n)
