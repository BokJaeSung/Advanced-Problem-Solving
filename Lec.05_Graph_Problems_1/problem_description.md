# Lec.05 Graph Problems (1) — Problem Descriptions

---

## PS.5.1 Lowest Common Ancestor

### Description
루트가 있는 트리에서 두 노드 u, v의 최소 공통 조상(LCA)을 구하시오.

### Input
첫째 줄에 노드의 개수 n이 주어진다.  
이후 n-1개의 줄에 간선 정보 a, b가 주어진다.  
다음 줄에 쿼리의 수 m이 주어진다.  
이후 m개의 줄에 쿼리 u, v가 주어진다.

### Output
각 쿼리에 대해 LCA를 한 줄에 하나씩 출력한다.

### Key Algorithm
- Binary Lifting (Sparse Table)
- parent[v][k] = v의 2^k번째 조상
- BFS로 depth · parent[v][0] 초기화 후 DP로 나머지 채우기
- T(n, m) = O((n + m) log n)

---

## PS.5.2 Distance on Tree

### Description
가중치가 있는 트리에서 두 노드 u, v 사이의 거리를 구하시오.

### Input
첫째 줄에 노드의 개수 n이 주어진다.  
이후 n-1개의 줄에 간선 정보 u, v, w가 주어진다.  
다음 줄에 쿼리의 수 m이 주어진다.  
이후 m개의 줄에 쿼리 u, v가 주어진다.

### Output
각 쿼리에 대해 두 노드 사이의 거리를 한 줄에 하나씩 출력한다.

### Key Algorithm
- LCA + 누적 거리
- dist(u, v) = dist[u] + dist[v] - 2 × dist[LCA(u, v)]
- T(n, m) = O((n + m) log n)

---

## PS.5.3 Range Minimum Query

### Description
수열이 주어졌을 때, 구간 [l, r]의 최솟값을 구하는 쿼리를 처리하시오.

### Input
첫째 줄에 수열의 크기 n이 주어진다.  
둘째 줄에 n개의 수열 원소가 주어진다.  
셋째 줄에 쿼리의 수 m이 주어진다.  
이후 m개의 줄에 쿼리 l, r이 주어진다 (0-indexed).

### Output
각 쿼리에 대해 구간 최솟값을 한 줄에 하나씩 출력한다.

### Key Algorithm
- Segment Tree (Bottom-up)
- 리프 노드: tree[n + i] = arr[i]
- 쿼리: 바텀업 방식으로 구간 탐색
- T(build) = O(n), T(query) = O(log n)
