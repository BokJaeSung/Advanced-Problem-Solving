# Lec.07 Graph Problems (3) — Problem Descriptions

---

## PS.7.1 Edge-Disjoint Paths

### Description
방향 그래프에서 소스 s에서 싱크 t로 가는 간선이 겹치지 않는 경로의 최대 개수를 구하시오.  
간선 겹치지 않는(Edge-Disjoint) 경로란, 어떤 두 경로도 같은 간선을 공유하지 않는 경로들을 말한다.

### Input
첫째 줄에 노드의 개수 n, 간선의 개수 m이 주어진다.  
이후 m개의 줄에 방향 간선 u, v가 주어진다.  
소스는 1번 노드, 싱크는 n번 노드이다.

### Output
간선이 겹치지 않는 경로의 최대 개수를 출력한다.

### Sample
```
Input:          Output:
6 8             2
1 2
1 3
2 4
3 4
2 5
3 6
4 6
5 6
```

### Key Algorithm
- Ford-Fulkerson (Edmonds-Karp, BFS)
- 각 간선의 용량을 1로 설정
- 최대 유량 = 간선 겹치지 않는 경로의 최대 수 (Max-Flow)
- T(n, m) = O(m² / n) ~ O(n × m) (Edmonds-Karp 기준)

---

## PS.7.2 Minimum Cut

### Description
방향 그래프에서 소스 s에서 싱크 t로의 최소 컷을 구하시오.  
최소 컷이란, 제거 시 s에서 t로의 모든 경로를 차단하는 간선 집합 중 용량 합이 최소인 것이다.

### Input
첫째 줄에 노드의 개수 n, 간선의 개수 m이 주어진다.  
이후 m개의 줄에 방향 간선 u, v, w(용량)가 주어진다.  
소스는 1번 노드, 싱크는 n번 노드이다.

### Output
첫째 줄에 최소 컷의 용량(= 최대 유량)을 출력한다.  
둘째 줄에 소스 측 노드 집합 S를 오름차순으로 출력한다.  
셋째 줄에 싱크 측 노드 집합 T를 오름차순으로 출력한다.

### Sample
```
Input:          Output:
6 8             3
1 2 2           1 2 3
1 3 1           4 5 6
2 4 1
2 5 1
3 4 2
4 6 2
5 6 1
3 5 1
```

### Key Algorithm
- Max-Flow Min-Cut 정리
- Ford-Fulkerson(Edmonds-Karp)으로 최대 유량 계산
- 잔여 그래프에서 s로부터 도달 가능한 노드 집합 S 결정
- S → V\S 간선이 최소 컷
- T(n, m) = O(n × m)

---

## PS.7.3 Bipartite Matching

### Description
이분 그래프에서 최대 매칭을 구하시오.  
이분 그래프는 노드가 좌측 집합 L과 우측 집합 R로 분리되며, 간선은 L↔R 사이에만 존재한다.

### Input
첫째 줄에 좌측 노드 수 L, 우측 노드 수 R, 간선의 개수 m이 주어진다.  
이후 m개의 줄에 간선 u, v가 주어진다.  
(u: 1~L의 좌측 노드, v: L+1~L+R의 우측 노드)

### Output
첫째 줄에 최대 매칭의 수를 출력한다.  
이후 매칭된 쌍 (u, v)를 한 줄에 하나씩 출력한다.

### Sample
```
Input:          Output:
3 3 5           3
1 4             1 4
1 5             2 5
2 4             3 6
2 5
3 6
```

### Key Algorithm
- Ford-Fulkerson (이분 매칭)
- 소스(0) → 좌측 노드(1~L) → 우측 노드(L+1~L+R) → 싱크(L+R+1) 구조
- 각 간선 용량 1
- 잔여 용량 0인 원래 간선 = 매칭된 쌍
- T(n, m) = O(n × m)
