import sys
input = sys.stdin.readline


def popcount(x):
    # bin(x) = '0b101...' 형태의 문자열 → '1'의 개수 = 켜진 비트 수
    return bin(x).count('1')


def is_vertex_cover(mask, edges):
    # mask의 각 비트가 정점 포함 여부를 나타냄 (bit i → 정점 i+1)
    for u, v in edges:
        # 간선 (u,v)의 양 끝점이 모두 cover에 없으면 vertex cover가 아님
        if not (mask & (1 << (u - 1))) and not (mask & (1 << (v - 1))):
            return False
    return True


def min_vertex_cover_bruteforce(n: int, edges: list) -> list:
    # T(n, m) = O(2^n * m)
    # 가능한 모든 정점 부분집합을 비트마스크로 열거 (0 ~ 2^n - 1)
    best = (1 << n) - 1  # 초기값: 전체 정점 집합 V
    for mask in range(1 << n):
        if is_vertex_cover(mask, edges):
            # 현재 cover 크기가 지금까지 최솟값보다 작으면 갱신
            if popcount(mask) < popcount(best):
                best = mask
    # best 마스크에서 켜진 비트 위치 → 정점 번호 (1-indexed)
    return [v for v in range(1, n + 1) if best & (1 << (v - 1))]


def min_vertex_cover_greedy(n: int, edges: list) -> list:
    # T(n, m) = O(n * m)
    # 2-approximation: 최적해의 최대 2배 이하 크기를 보장
    cover = 0       # 선택된 정점 집합 (비트마스크)
    F = list(edges) # 아직 커버되지 않은 간선 목록
    while F:
        u, v = F.pop()              # 임의의 간선 하나 선택
        cover |= 1 << (u - 1)      # 양 끝점 u, v를 모두 cover에 추가
        cover |= 1 << (v - 1)
        # u 또는 v에 인접한 간선은 이미 커버됨 → 제거
        F = [e for e in F if not (u in e or v in e)]
    return [v for v in range(1, n + 1) if cover & (1 << (v - 1))]


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

if n < 16:
    # n < 16: brute-force로 정확한 최솟값 탐색
    S = min_vertex_cover_bruteforce(n, edges)
else:
    # n >= 16: greedy 2-approximation (최적해의 2배 이하 보장)
    S = min_vertex_cover_greedy(n, edges)

print(len(S))
print(*S)
