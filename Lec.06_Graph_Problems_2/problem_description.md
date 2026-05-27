# Lec.06 Graph Problems (2) — Problem Descriptions

---

## PS.6.1 Kosaraju (SCC)

### Description
방향 그래프가 주어졌을 때, 강한 연결 요소(SCC)를 구하시오.  
SCC란 서로 도달 가능한 노드들의 최대 집합이다.  
Kosaraju 알고리즘은 원래 그래프와 역방향 그래프에서 각각 DFS를 수행하여 SCC를 추출한다.

### Input
첫째 줄에 노드의 개수 n, 간선의 개수 m이 주어진다.  
이후 m개의 줄에 방향 간선 u, v가 주어진다.

### Output
첫째 줄에 SCC의 개수를 출력한다.  
이후 각 SCC를 한 줄에 하나씩 오름차순으로 출력한다.  
SCC들은 사전순으로 정렬하여 출력한다.

### Sample
```
Input:          Output:
9 12            4
1 4             1 2 5
4 7             3 4 6 8
7 1             7
6 7             9
8 5
5 9
9 6
9 8
2 6
2 3
3 2
4 2
```

### Key Algorithm
- Kosaraju's Algorithm
- 1단계: 원래 그래프에서 DFS → 완료 순서 스택 저장
- 2단계: 역방향 그래프에서 스택 역순으로 DFS → 각 SCC 추출
- T(n, m) = O(n + m)

---

## PS.6.2 Tarjan (SCC)

### Description
방향 그래프가 주어졌을 때, 강한 연결 요소(SCC)를 구하시오.  
SCC란 서로 도달 가능한 노드들의 최대 집합이다.  
Tarjan 알고리즘은 DFS 한 번만으로 SCC를 추출하며, disc/low 값과 스택을 활용한다.

### Input
첫째 줄에 노드의 개수 n, 간선의 개수 m이 주어진다.  
이후 m개의 줄에 방향 간선 u, v가 주어진다.

### Output
첫째 줄에 SCC의 개수를 출력한다.  
이후 각 SCC를 한 줄에 하나씩 오름차순으로 출력한다.  
SCC들은 사전순으로 정렬하여 출력한다.

### Sample
```
Input:          Output:
9 12            4
1 4             1 2 5
4 7             3 4 6 8
7 1             7
6 7             9
8 5
5 9
9 6
9 8
2 6
2 3
3 2
4 2
```

### Key Algorithm
- Tarjan's Algorithm
- DFS 한 번으로 SCC 추출
- disc[v]: 방문 순서, low[v]: 도달 가능한 최소 disc
- 스택으로 현재 경로 관리; low[v] == disc[v]이면 SCC 완성
- T(n, m) = O(n + m)

---

## PS.6.3 Minimum Source Cover

### Description
방향 그래프에서 모든 노드에 도달할 수 있는 최소 출발 노드 집합의 크기를 구하시오.  
즉, 선택한 노드들로부터 BFS/DFS를 수행했을 때 그래프의 모든 노드를 방문할 수 있어야 한다.

### Input
첫째 줄에 노드의 개수 n, 간선의 개수 m이 주어진다.  
이후 m개의 줄에 방향 간선 u, v가 주어진다.

### Output
최소 출발 노드 집합의 크기를 출력한다.

### Sample
```
Input:          Output:
9 12            2
1 4
4 7
7 1
6 7
8 5
5 9
9 6
9 8
2 6
2 3
3 2
4 2
```

### Key Algorithm
- SCC 축약 후 in-degree = 0인 SCC 노드 선택
- Kosaraju / Tarjan → DAG 변환 → in-degree 0 카운트
- T(n, m) = O(n + m)

---

## PS.6.4 2-SAT

### Description
2-SAT 문제가 주어졌을 때, 만족 가능 여부를 판단하시오.  
각 절(clause)은 두 리터럴의 OR이며, 모든 절을 참으로 만드는 변수 할당이 존재하는지 출력한다.  
변수 i는 양수(i)와 음수(-i)로 표현한다.

### Input
첫째 줄에 변수의 개수 n, 절(clause)의 개수 m이 주어진다.  
이후 m개의 줄에 절을 구성하는 두 리터럴 u, v가 주어진다.  
(양수: 변수 그대로, 음수: NOT 변수)

### Output
만족 가능하면 `True`, 불가능하면 `False`를 출력한다.

### Sample
```
Input:          Output:
3 4             True
1 2
-1 3
-2 -3
1 -3
```

### Key Algorithm
- 함의 그래프(Implication Graph) 구성: (u ∨ v) → (¬u → v) ∧ (¬v → u)
- SCC로 각 변수의 참/거짓 결정
- x와 ¬x가 같은 SCC에 속하면 UNSATISFIABLE
- T(n, m) = O(n + m)
