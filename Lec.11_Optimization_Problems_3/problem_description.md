# Lec.11 Optimization Problems (3) — Problem Descriptions

---

## PS.11.1 Minimum Vertex Cover

### Description
방향이 없는 그래프 G=(V,E)가 주어졌을 때, 크기가 가장 작은 정점 덮개와 그 길이를 구하시오.

정점 덮개(vertex cover)란, 정점 집합 V의 부분 집합 S 중에서  
모든 간선이 S에 포함된 정점에 최소한 하나 이상 연결되는 집합을 말한다.

### Input
첫째 줄에 정점의 개수 n, 간선의 개수 m이 주어진다.  
1 ≤ n ≤ 1,000, 1 ≤ m ≤ 1,000,000  
이후 m개의 줄에 간선 u, v가 주어진다.

### Output
첫째 줄에 정점 덮개의 길이를 출력한다.  
둘째 줄에 각 정점 덮개의 원소를 오름차순으로 출력한다.

### Key Algorithm
- n < 16: Brute-Force (비트마스크 열거, O(2^n × m))
- n ≥ 16: Greedy 2-Approximation (임의 간선 선택 후 양 끝점 추가, O(n × m))

---

## PS.11.2 Minimum Set Cover

### Description
전체 집합 X(1~n)와 부분 집합의 패밀리 F(m개)가 주어졌을 때,  
F의 부분집합 중 합집합이 X가 되는 가장 작은 집합 덮개 C를 구하시오.

### Input
첫째 줄에 X의 크기 n, F의 크기 m이 주어진다.  
1 ≤ n ≤ 1,000, 1 ≤ m ≤ 1,000  
둘째 줄부터 m개의 줄에 각 부분 집합이 주어진다.

### Output
첫째 줄에 C의 크기를 출력한다.  
둘째 줄부터 C에 포함된 각 부분 집합을 한 줄에 하나씩 출력한다.

### Key Algorithm
- m < 16: Brute-Force (비트마스크 열거, O(2^m × m))
- m ≥ 16: Greedy ln(n)+1 Approximation (매 단계 가장 많이 커버하는 집합 선택, O(n × m))
