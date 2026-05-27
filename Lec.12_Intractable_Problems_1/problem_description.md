# Lec.12 Intractable Problems (1) — Problem Descriptions

---

## PS.12.1 Sudoku Puzzle

### Description
Sudoku 퍼즐이 주어질 때, 솔루션을 출력하시오.

표준 Sudoku 퍼즐은 9×9 그리드 구조이고, 다음 조건을 만족한다.
1. 각 행은 1부터 9까지의 숫자를 정확히 하나씩만 가진다.
2. 각 열은 1부터 9까지의 숫자를 정확히 하나씩만 가진다.
3. 각 3×3 부분 그리드(박스)는 1부터 9까지의 숫자를 정확히 하나씩만 가진다.

단, 모든 입력은 정확히 하나의 솔루션만 갖고 있음이 보장된다.

### Input
표준 9×9 Sudoku 퍼즐이 주어진다. 빈 칸은 0으로 주어진다.

### Output
Sudoku 퍼즐의 솔루션을 출력한다.

### Key Algorithm
- Backtracking + MRV (Minimum Remaining Values)
- 비트마스크로 행·열·박스 사용 숫자 관리
- 후보가 가장 적은 칸 먼저 채움 → 가지치기 효율 극대화
- 첫 솔루션 발견 시 즉시 True 반환 (조기 종료)

---

## PS.12.2 Unique Sudoku

### Description
Sudoku 퍼즐이 주어질 때, 이 퍼즐의 솔루션이 유일한 해를 갖는지를 판단하시오.  
단, 주어지는 입력 퍼즐은 유효한 퍼즐임을 보장한다. (솔루션이 1개 이상)

### Input
표준 9×9 퍼즐이 주어진다. 빈 칸은 0으로 주어진다.

### Output
Sudoku 퍼즐이 유일한 해를 가지면 "YES"를 출력한다.  
아니면, "NO"를 출력한다.

### Key Algorithm
- PS.12.1과 동일한 Backtracking + MRV
- count 전역변수로 솔루션 수 카운트
- count ≥ 2 이면 즉시 탐색 종료 (조기 종료)

---

## PS.12.3 Load Balancing

### Description
n개의 작업(job)이 각 작업의 처리 시간과 함께 주어질 때, k명의 일꾼(worker)에게 모든 작업을 배정하려고 한다.  
각 일꾼이 배정받은 모든 작업을 처리하는 데 걸리는 시간을 load_i라 할 때,  
모든 load_i의 최댓값을 최소로 배정하려 할 때, 그 최솟값을 구하시오.

### Input
첫째 줄에 작업의 개수 n과 일꾼의 인원 수 k가 주어진다.  
둘째 줄에 n개의 작업 시간이 주어진다.

### Output
각 일꾼이 배정받은 작업을 모두 끝내는 데 필요한 시간의 최댓값의 최솟값을 출력한다.

### Key Algorithm
- Branch & Bound (Best-First Search)
- 작업 내림차순 정렬 + suffix_sum 사전 계산
- lower_bound = max(현재 최대 부하, ceil(전체합 / k))
- greedy_upper_bound로 초기 best 설정
- 대칭 가지치기 (동일 부하 일꾼 중복 배정 방지)
- 동치 상태 통합 (loads 정렬 후 tuple로 visited 관리)
