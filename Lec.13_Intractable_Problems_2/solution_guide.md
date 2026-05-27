# Lec.13 Intractable Problems (2) — 풀이 설명

---

## PS.13.1 — Traveling Salesperson Problem (TSP)

### 문제 핵심

0번에서 출발해 모든 도시를 **정확히 한 번씩** 방문하고 0번으로 돌아오는 경로 중 **최소 비용** 경로를 찾는 문제.

완전 탐색하면 $(n-1)!$ 개의 순열을 모두 시도해야 해서 $n=16$에서 약 $1.3 \times 10^{12}$번 → 불가능.  
**DP + 비트마스킹** 으로 $O(n^2 \cdot 2^n)$ 으로 줄인다.

---

### 핵심 아이디어: Held-Karp 알고리즘

**상태 정의**

```
dp[mask][v] = 0번에서 출발해, mask에 표시된 도시들을 방문하고,
              현재 v에 있을 때의 최소 비용
```

- `mask`의 bit `i` → 도시 `i+1` 방문 여부  
  (도시 0은 항상 출발점이므로 마스크에서 제외 → mask 크기 `2^(n-1)`)

**점화식**

```
dp[mask | (1<<(v-1))][v] = min(dp[mask][u] + W[u][v])
    (v가 mask에 없을 때, 모든 u에 대해)
```

**초기값 / 종료**

```
dp[0][0] = 0          # 0번에서 출발, 아무도 안 방문
full = (1<<(n-1)) - 1  # 모든 도시 방문 완료 마스크

정답 = min(dp[full][v] + W[v][0])  for v in 1..n-1
```

---

### 경로 복원 (reconstruct)

`path[mask][v] = u` : 상태 `(mask, v)`에 도달하기 직전 도시가 `u`  
full mask에서 시작해 `mask ^= 1 << (cur-1)` 로 도시를 하나씩 제거하며 역추적.

```
full → last_city → ... → 0  (역순 저장 후 뒤집기)
```

---

### 복잡도

| | 값 |
|---|---|
| 상태 수 | $2^{n-1} \times n$ |
| 전이 | 각 상태에서 $O(n)$ |
| **전체** | $O(n^2 \cdot 2^n)$ |
| 공간 | $O(n \cdot 2^n)$ |

$n=16$ → 약 $8 \times 10^6$ 연산 → 충분히 가능.

---

### 흐름 요약

```
1. W 인접 행렬 초기화 (없는 간선 = INF)
2. dp[0][0] = 0 으로 시작
3. 모든 (mask, u) 상태에서 갈 수 있는 v로 전이 → dp 갱신
4. full 상태에서 0번 복귀 비용 최솟값 → 정답 비용
5. path 테이블 역추적 → tour 복원
```

---

---

## PS.13.2 — Shortest Superstring

### 문제 핵심

$n$개의 단어를 모두 부분 문자열로 포함하는 **가장 짧은 문자열**의 길이를 구하는 문제.

단어들을 최대한 겹쳐서 이어 붙이면 전체 길이가 줄어든다.  
**어떤 순서로 이어 붙이느냐** 가 핵심 → TSP와 동일한 구조.

---

### 핵심 아이디어: TSP로 변환

**overlap[i][j]** : 단어 `i`의 접미사와 단어 `j`의 접두사가 겹치는 최대 길이

```
nodes[i] = "abcd",  nodes[j] = "cdef"
overlap[i][j] = 2   ("cd" 겹침)
```

**간선 가중치 W[i][j]** : `i` 다음에 `j`를 이어 붙일 때 **추가되는 문자 수**

```
W[i][j] = len(nodes[j]) - overlap[i][j]
```

이렇게 정의하면 **W의 합을 최소화** = **superstring 길이 최소화**.

---

### TSP와의 차이점

| | TSP (1번) | Shortest Superstring (2번) |
|---|---|---|
| 노드 0 | 실제 출발 도시 | dummy `""` (어떤 단어든 첫 시작 허용) |
| 출발점 복귀 | ✅ `dp[full][v] + W[v][0]` | ❌ `dp[full][v]` 그대로 (Hamiltonian path) |
| 간선 가중치 | 실제 거리 | `len(j) - overlap[i][j]` |

**dummy 노드가 필요한 이유**  
TSP DP 코드는 0번에서 출발하도록 고정되어 있다.  
어떤 단어든 첫 번째로 올 수 있어야 하므로, 길이 0인 `""` 를 0번 노드로 추가하면  
`W[0][j] = len(j) - 0 = len(j)` → dummy에서 어느 단어로든 동일하게 시작 가능.

---

### 흐름 요약

```
1. nodes = [""] + words  (dummy 추가, 총 n+1개)
2. overlap[i][j] 계산  (접미사-접두사 겹침)
3. W[i][j] = len(nodes[j]) - overlap[i][j]
4. tsp_dp(n+1, W) 실행  (복귀 없는 Hamiltonian path 최솟값)
5. 결과 출력
```

---

---

## PS.13.3 — Euclidean TSP (MST Heuristic)

### 문제 핵심

평면 위 $n$개의 점에서 모든 점을 방문하고 돌아오는 TSP tour를 구하되,  
$n \leq 1000$ 이므로 DP ($O(n^2 \cdot 2^n)$)는 불가능.  
대신 **MST 기반 근사 알고리즘** 으로 **최적해의 2배 이하** 를 보장하는 tour를 출력.

---

### 핵심 아이디어: MST-Heuristic (2-approximation)

**왜 MST인가?**

최적 TSP tour에서 간선 하나를 제거하면 spanning tree가 된다.  
→ MST 가중치 합 ≤ 최적 TSP 비용  
→ MST를 기반으로 tour를 만들면 최적해의 **2배 이하** 보장.

**알고리즘 3단계**

```
1. Prim으로 MST 구성
2. MST를 DFS preorder 순서로 방문
3. 방문 순서 = TSP tour 근사해
```

---

### Step 1: Prim's Algorithm

```
distance[v] = v를 MST에 연결하는 현재까지 발견된 최소 간선 가중치
parent[v]   = v를 MST에 연결하는 정점

매 단계: distance가 가장 작은 미방문 정점 u 선택 → MST에 추가
        → u의 이웃들 distance 갱신
```

$O(n^2)$ 선형 탐색 구현 (힙 없이, $n \leq 1000$ 이므로 충분).

**`round()` 가 필요한 이유**  
`sqrt()` 결과는 부동소수점 → 두 거리가 거의 같을 때 오차로 MST 구조가 달라짐.  
`round()` 로 정수 단위 거리를 쓰면 채점 기준과 동일한 MST가 만들어진다.  
(실험: 1000번 랜덤 테스트에서 `round()` 없이 쓰면 32%에서 MST가 달라짐)

---

### Step 2: DFS Preorder

MST 위에서 DFS를 돌며 **처음 방문하는 순서대로** 노드를 기록.

```
      0
     / \
    1   2
   / \
  3   4

Preorder: 0 → 1 → 3 → 4 → 2
```

**재귀 대신 스택 사용**  
Python 기본 재귀 한도 = 1000, $n \leq 1000$ 이면 초과 위험.  
스택 기반 iterative DFS로 구현하되, **역순 삽입** 으로 preorder 유지.

---

### 2-approximation 보장 이유

```
MST 비용 ≤ OPT          (MST는 spanning tree 중 최솟값)
DFS tour ≤ 2 × MST 비용  (각 간선을 최대 2번 통과)
→ DFS tour ≤ 2 × OPT
```

삼각부등식($d(A,C) \leq d(A,B) + d(B,C)$)이 성립하는 유클리드 거리에서만 보장.

---

### 복잡도 비교

| 알고리즘 | 복잡도 | 결과 |
|---|---|---|
| DP (Held-Karp) | $O(n^2 \cdot 2^n)$ | 최적해 |
| MST Heuristic | $O(n^2)$ | 최적해의 2배 이하 |

$n = 16$ → DP 가능.  
$n = 1000$ → MST Heuristic 필수.
