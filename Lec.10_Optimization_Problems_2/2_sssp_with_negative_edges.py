import sys
input = sys.stdin.readline
from collections import defaultdict

def init_single_source(graph, source):
    # 모든 노드의 초기 거리를 무한대로 설정
    dist = {v: float('inf') for v in graph}
    dist[source] = 0  # 출발점 자신까지의 거리는 0
    parent = {v: None for v in graph}  # 경로 역추적용 직전 노드
    return dist, parent

def relax(u, v, w, dist, parent):
    # u를 거쳐 v로 가는 거리가 더 짧으면 갱신
    # 다익스트라의 relax와 달리 반환값 없음 (벨만포드는 모든 엣지를 무조건 순회하므로)
    if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        parent[v] = u

def bellman_ford(graph, source):
    dist, parent = init_single_source(graph, source)

    # 모든 엣지를 리스트로 펼쳐두기 (매 라운드마다 전체 순회)
    edges = [(u, v, w) for u in graph for v, w in graph[u]]

    # V-1번 반복: 라운드 k가 끝나면 k개 엣지 이하 최단경로 확정
    for _ in range(len(graph) - 1):
        for u, v, w in edges:
            relax(u, v, w, dist, parent)

    # V-1번 후에도 갱신이 발생하면 → 음수 사이클 존재
    # (정상이라면 이미 최적이라 더 줄어들 수 없어야 함)
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None, None  # 음수 사이클 → 최단경로 정의 불가

    return dist, parent

def reconstruct_path(parent, s, t):
    path = []
    cur = t
    # t에서 parent를 역추적하며 s까지 올라감
    while cur is not None:
        path.append(cur)
        if cur == s:
            break
        cur = parent[cur]
    else:
        # while 루프가 break 없이 끝남 = s에 도달 못 함 = 경로 없음
        return None
    path.reverse()  # 역추적했으므로 뒤집어서 s→t 순서로
    return path

def main():
    n, m = map(int, input().split())

    # defaultdict(list) + 노드 초기화: 간선 없는 노드도 graph에 포함시키기 위해
    graph = defaultdict(list)
    for i in range(1, n + 1):
        graph[i]  # 키만 등록 (빈 리스트), 간선 없는 고립 노드 처리용

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))  # 방향 그래프: u→v

    q = int(input())
    queries = []
    for _ in range(q):
        s, t = map(int, input().split())
        queries.append((s, t))

    # 같은 출발점 s에 대해 벨만포드를 중복 실행하지 않도록 캐싱
    cache = {}
    for s, t in queries:
        if s not in cache:
            cache[s] = bellman_ford(graph, s)  # 처음 등장한 출발점만 계산
        dist, parent = cache[s]

        if dist is None:
            # bellman_ford가 None 반환 = 음수 사이클 존재
            print("There is a negative cycle.")
        elif dist[t] == float('inf'):
            # dist[t]가 여전히 무한대 = s에서 t로 가는 경로 없음
            print(f"There is no path from {s} to {t}.")
        else:
            path = reconstruct_path(parent, s, t)
            print(" -> ".join(map(str, path)) + f": {dist[t]}")

if __name__ == "__main__":
    main()
