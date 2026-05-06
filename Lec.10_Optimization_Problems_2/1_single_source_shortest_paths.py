from heapq import heappush, heappop  # 최소 힙 연산 (우선순위 큐)

def init_single_source(graph, source):
    # 모든 노드의 초기 거리를 무한대로 설정 (아직 아무것도 모르는 상태)
    dist = {v: float('inf') for v in graph}
    # 각 노드의 직전 노드를 None으로 초기화 (경로 역추적용)
    parent = {v: None for v in graph}
    # 출발점 자신까지의 거리는 0
    dist[source] = 0
    return dist, parent

def relax(u, v, w, dist, parent):
    # u를 거쳐서 v로 가는 거리가 현재 알려진 dist[v]보다 짧으면 갱신
    if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w  # 더 짧은 경로 발견 → 거리 업데이트
        parent[v] = u           # v로 오는 최적 경로에서 직전 노드는 u
        return True             # 갱신 발생 → 힙에 다시 넣어야 함
    return False                # 갱신 없음

def dijkstra(graph, source):
    dist, parent = init_single_source(graph, source)

    # (거리, 노드) 형태로 최소 힙 운용 → 항상 가장 가까운 노드부터 처리
    PQ = [(0, source)]
    visited = set()  # 이미 최단거리가 확정된 노드들

    while PQ:
        _, u = heappop(PQ)  # 현재 가장 거리가 짧은 노드 꺼내기

        # 이미 방문한 노드면 스킵 (힙에 중복으로 들어갔을 수 있음)
        if u in visited:
            continue
        visited.add(u)  # u의 최단거리 확정

        for v, w in graph[u]:       # u의 모든 인접 노드 v, 가중치 w
            if v not in visited:    # 아직 확정 안 된 노드만 시도
                if relax(u, v, w, dist, parent):  # 거리 갱신 성공하면
                    heappush(PQ, (dist[v], v))    # 갱신된 거리로 힙에 추가

    return dist, parent

def shortest_path(s, t, parent):
    # 출발점 == 도착점이면 자기 자신만 반환
    if s == t:
        return [t]
    # parent[t]가 None이면 s에서 t로 오는 경로가 없음
    elif parent[t] is None:
        return [None]
    else:
        # t의 직전 노드(parent[t])까지의 경로를 재귀로 구하고, 맨 끝에 t 붙이기
        # 예: s=1, t=4, parent = {4:3, 3:2, 2:1}
        #   → shortest_path(1,3) + [4]
        #   → shortest_path(1,2) + [3] + [4]
        #   → [1,2,3,4]
        return shortest_path(s, parent[t], parent) + [t]


# ── 입력 ──────────────────────────────────────────────
n, m = map(int, input().split())  # 정점 수, 간선 수

# 인접 리스트: graph[u] = [(v, w), ...] 형태
graph = {v: [] for v in range(1, n + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # 방향 그래프이므로 u→v 방향만 추가

# ── 쿼리 처리 ─────────────────────────────────────────
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())

    # 매 쿼리마다 s를 출발점으로 다익스트라 실행
    dist, parent = dijkstra(graph, s)

    # parent 테이블을 역추적해서 실제 경로 복원
    path = shortest_path(s, t, parent)

    if path[0] is None:
        # t에 도달하는 경로가 없는 경우
        print(f"There is no path from {s} to {t}.")
    else:
        # [1, 2, 3, 4] → "1 -> 2 -> 3 -> 4: 7" 형식으로 출력
        print(" -> ".join(map(str, path)) + f": {dist[t]}")
