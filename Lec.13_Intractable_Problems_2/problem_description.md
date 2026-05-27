# Lec.13 Intractable Problems (2) — Problem Descriptions

---

## PS.13.1 Traveling Salesperson Problem

### Description
가중치가 있는 방향 그래프 G=(V,E)가 주어지고, 정점의 집합 V={0,1,…,n-1}에서 출발 정점을 0이라고 가정한다.  
0번 정점으로부터 다른 모든 정점을 정확히 한 번씩만 방문하고 0번 정점으로 되돌아 오는 경로(tour) 중에서  
경로의 간선 가중치의 합이 최소가 되는 tour를 출력하시오.

단, 이 문제는 강의자료에 있는 DP 솔루션으로 최적값과 최적해를 찾아 출력해야 한다.

### Input
첫째 줄에 정점의 개수 n과 간선의 개수 m이 주어진다. (1 ≤ n ≤ 16)  
이후 m개의 줄에 간선 정보 u, v, w가 주어진다.

### Output
첫째 줄에 최단 tour의 경로 길이를 출력한다.  
둘째 줄에 최단 tour를 출력한다.

### Key Algorithm
- Held-Karp DP (비트마스킹)
- dp[mask][v] = 0번 출발, mask 도시들 방문 후 v에 있을 때 최소 비용
- bit i → 도시 i+1 방문 여부
- path 테이블 역추적으로 tour 복원
- T(n) = O(n² × 2^n)

---

## PS.13.2 Shortest Superstring

### Description
n개의 영문자로 구성된 단어가 주어졌을 때,  
주어진 모든 단어를 부분 문자열로 모두 포함하는 superstring 중에서  
길이가 가장 짧은 superstring의 길이를 출력하시오.

단, 주어지는 단어들은 중복되는 단어가 없고, 어떠한 단어도 다른 단어의 부분 문자열은 아니라고 가정해도 된다.

### Input
첫째 줄에 단어의 개수 n이 주어진다. (1 ≤ n ≤ 16)  
둘째 줄부터 n개의 줄에 한 줄에 하나씩 단어가 주어진다. (알파벳 소문자)

### Output
첫째 줄에 길이가 가장 짧은 superstring의 길이를 출력한다.

### Key Algorithm
- TSP DP로 변환 (Hamiltonian Path, 복귀 없음)
- dummy start node ("") 추가 → 어떤 단어든 첫 시작 허용
- overlap[i][j] = 접미사-접두사 겹침 최대 길이
- W[i][j] = len(nodes[j]) - overlap[i][j] (추가 문자 수)
- T(n) = O(n² × 2^n)

---

## PS.13.3 Euclidean TSP

### Description
n개의 평면 위의 점들의 좌표값이 주어졌을 때,  
첫 번째 점에서 출발해서 모든 점들을 방문하고 출발한 점으로 되돌아 오는 선들 중에서  
MST-heuristic 전략으로 찾을 수 있는 TSP tour를 출력하시오.

단, 이 문제는 강의자료에서 제시한 Prim's 알고리즘을 이용한 휴리스틱 솔루션을 출력해야 한다.

### Input
첫째 줄에 좌표값의 개수 n이 주어진다. (1 ≤ n ≤ 1,000)  
둘째 줄부터 n개의 줄에 좌표값 x, y가 주어진다.

### Output
첫째 줄에 MST-heuristic으로 찾은 근사해의 경로를 출력한다.

### Key Algorithm
- Prim's Algorithm으로 MST 구성 (O(n²), 선형 탐색)
- DFS Preorder로 MST 방문 순서 = TSP tour
- 2-approximation 보장 (삼각부등식 성립 시)
- round()로 부동소수점 오차 제거 (간선 선택 기준 통일)
- T(n) = O(n²)
