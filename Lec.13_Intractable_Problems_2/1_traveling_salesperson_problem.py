import sys
input = sys.stdin.readline

INF = float('inf')


def min_cost(n: int, W: list, dp: list) -> tuple:
    # 모든 도시(1~n-1)를 방문한 상태(full)에서 0번으로 복귀하는 최소 비용 탐색
    full = (1 << (n - 1)) - 1  # 1~n-1번 도시 모두 방문한 비트마스크
    best_cost = INF
    last_city = -1
    for v in range(1, n):
        cost = dp[full][v] + W[v][0]  # 마지막 도시 v → 출발점 0 복귀 비용
        if cost < best_cost:
            best_cost = cost
            last_city = v
    return best_cost, last_city


def reconstruct(n: int, path: list, last_city: int) -> list:
    # path 테이블을 역추적해 방문 순서 복원
    order = []
    mask = (1 << (n - 1)) - 1  # full mask에서 시작
    cur = last_city
    while cur != 0 and cur != -1:
        order.append(cur)
        prev = path[mask][cur]
        mask ^= 1 << (cur - 1)  # cur 도시를 방문 집합에서 제거
        cur = prev
    return [0] + list(reversed(order)) + [0]


def tsp_dp(n: int, W: list) -> tuple:
    # T(n) = O(n^2 * 2^n)
    # dp[mask][v]: 0번 출발, mask에 속한 도시들을 방문하고 v에 있을 때 최소 비용
    # mask의 bit i → 도시 i+1 방문 여부 (도시 0은 항상 출발점이므로 마스크에서 제외)
    dp   = [[INF] * n for _ in range(1 << (n - 1))]
    path = [[-1]  * n for _ in range(1 << (n - 1))]
    dp[0][0] = 0  # 출발: 아무 도시도 안 방문, 0번에 위치, 비용 0

    for mask in range(1 << (n - 1)):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(1, n):
                if mask & (1 << (v - 1)):  # v 이미 방문 → 스킵
                    continue
                next_mask = mask | (1 << (v - 1))  # v를 방문 집합에 추가
                next_cost = dp[mask][u] + W[u][v]
                if next_cost < dp[next_mask][v]:
                    dp[next_mask][v] = next_cost
                    path[next_mask][v] = u  # v 직전 도시 = u 기록

    cost, last = min_cost(n, W, dp)
    if cost == INF:
        return INF, []
    tour = reconstruct(n, path, last)
    return cost, tour


n, m = map(int, input().split())

# 인접 행렬 초기화
W = [[INF] * n for _ in range(n)]
for v in range(n):
    W[v][v] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w

cost, tour = tsp_dp(n, W)
if cost == INF:
    print("No tour")
else:
    print(cost)
    print(*tour)
