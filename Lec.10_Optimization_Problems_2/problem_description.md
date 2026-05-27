# Lec.10 Optimization Problems (2) — Problem Descriptions

---

## PS.10.1 Single Source Shortest Paths (SSSP)

### Description
가중치가 있는 방향 그래프에서 출발 정점 s로부터 도착 정점 t까지의 최단 경로를 구하시오.  
간선 가중치는 0 이상의 정수이다.

### Input
첫째 줄에 정점의 개수 n, 간선의 개수 m이 주어진다.  
이후 m개의 줄에 간선 정보 u, v, w가 주어진다.  
다음 줄에 쿼리의 수 q가 주어진다.  
이후 q개의 줄에 출발 정점 s, 도착 정점 t가 주어진다.

### Output
각 쿼리에 대해 최단 경로를 `노드1 -> 노드2 -> ... -> 노드k: 거리` 형식으로 출력한다.  
경로가 없으면 `There is no path from s to t.`를 출력한다.

### Sample
```
Input:                  Output:
5 7                     1 -> 2 -> 4: 5
1 2 2                   1 -> 3 -> 5: 7
1 3 4                   There is no path from 4 to 1.
2 3 1
2 4 3
3 4 5
3 5 3
4 5 2
3
1 4
1 5
4 1
```

### Key Algorithm
- Dijkstra (Lazy Deletion, heapq)
- (거리, 노드) 형태 최소 힙 운용 → 항상 가장 가까운 노드부터 확정
- visited 집합으로 중복 처리 방지
- parent 테이블 역추적으로 경로 복원
- T(n, m) = O(m log n)

---

## PS.10.2 SSSP with Negative Edges

### Description
음수 간선이 있는 방향 그래프에서 출발 정점 s로부터 도착 정점 t까지의 최단 경로를 구하시오.  
음수 사이클이 존재하는 경우에는 이를 감지하여 출력한다.

### Input
첫째 줄에 정점의 개수 n, 간선의 개수 m이 주어진다.  
이후 m개의 줄에 간선 정보 u, v, w가 주어진다. (w는 음수일 수 있음)  
다음 줄에 쿼리의 수 q가 주어진다.  
이후 q개의 줄에 출발 정점 s, 도착 정점 t가 주어진다.

### Output
각 쿼리에 대해 최단 경로를 `노드1 -> 노드2 -> ... -> 노드k: 거리` 형식으로 출력한다.  
음수 사이클이 존재하면 `There is a negative cycle.`을 출력한다.  
경로가 없으면 `There is no path from s to t.`를 출력한다.

### Sample
```
Input:                  Output:
4 5                     1 -> 2 -> 3: 1
1 2 3                   1 -> 2 -> 3 -> 4: 3
1 3 4
2 3 -2
3 4 2
4 2 -5
2
1 3
1 4
```

> 음수 사이클 예시 (2→3→4→2, 합 = -2+2-5 = -5 < 0) 포함 시:
> ```
> Output: There is a negative cycle.
> ```

### Key Algorithm
- Bellman-Ford
- |V|-1번 모든 간선 relaxation → k번 반복 후 k개 이하 엣지 최단경로 확정
- n번째 반복에서 갱신 발생 → 음수 사이클 존재
- 같은 출발점 s의 중복 쿼리는 캐싱으로 처리
- T(n, m) = O(n × m)

---

## PS.10.3 Sliding Puzzle

### Description
n×n 슬라이딩 퍼즐이 주어졌을 때, 목표 상태까지의 최소 이동 횟수를 구하시오.  
목표 상태는 1, 2, …, n²-1이 순서대로 나열되고 빈 칸(0)이 오른쪽 하단에 위치한 상태이다.  
풀 수 없으면 -1을 출력한다.

### Input
첫째 줄에 n이 주어진다.  
이후 n개의 줄에 퍼즐 상태가 주어진다. (빈 칸 = 0)

### Output
최소 이동 횟수를 출력한다. 풀 수 없으면 -1.

### Sample
```
Input:      Output:
3           5
1 2 3
4 0 5
7 8 6
```

### Key Algorithm
- 풀이 가능 여부: 반전(Inversion) 수 홀짝성 판별
  - n 홀수: inv % 2 == 0 이면 가능
  - n 짝수: (inv + 빈칸 행 번호) % 2 == 1 이면 가능
- 3×3: BFS (상태 수 9! = 362,880)
- 4×4 이상: A* (맨해튼 거리 휴리스틱, admissible)
- T = O(b^d) (b = 분기 수, d = 깊이)
