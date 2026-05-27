import sys
from math import sqrt
input = sys.stdin.readline

INF = float('inf')


def dist(p1, p2):
    # round()로 반올림하여 정수 단위 거리 사용
    # 이유: float 그대로 쓰면 소수점 오차로 인해 두 거리가 실제로 같거나
    #       거의 같을 때 어느 간선을 MST에 포함할지 달라져 tour 순서가 바뀜
    #       → 채점 기준(정수 거리)과 MST 구조를 맞추기 위해 round() 필요
    return round(sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))


def prim(n: int, points: list) -> list:
    # T(n) = O(n^2) — 선형 탐색으로 최솟값 추출 (n <= 1000 이므로 충분)
    visited  = [False] * n
    distance = [INF] * n  # 각 정점을 MST에 연결하는 최소 간선 가중치
    parent   = [-1] * n
    distance[0] = 0.0     # 0번 정점에서 시작

    for _ in range(n):
        # 아직 MST에 포함되지 않은 정점 중 distance가 가장 작은 정점 선택
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or distance[v] < distance[u]):
                u = v
        visited[u] = True

        # u의 이웃 정점들의 distance 갱신
        for v in range(n):
            if not visited[v]:
                d = dist(points[u], points[v])
                if d < distance[v]:
                    distance[v] = d
                    parent[v] = u

    return parent


def preorder(n: int, mst: dict, start: int = 0) -> list:
    # MST를 DFS preorder 순서로 방문 → TSP tour 근사해
    # 재귀 대신 스택으로 구현 (n <= 1000, 재귀 한도 초과 방지)
    visited = [False] * n
    tour = []
    stack = [start]
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        tour.append(u)
        # preorder 유지를 위해 역순으로 삽입
        for v in reversed(mst[u]):
            if not visited[v]:
                stack.append(v)
    return tour


def tsp_mst(n: int, points: list) -> list:
    parent = prim(n, points)

    # parent 배열로 MST 인접 리스트 구성 (무방향)
    graph = {v: [] for v in range(n)}
    for v in range(1, n):
        u = parent[v]
        graph[u].append(v)
        graph[v].append(u)

    tour = preorder(n, graph, start=0)
    return tour


n = int(input())
points = [tuple(map(float, input().split())) for _ in range(n)]

tour = tsp_mst(n, points)
print(*tour)
