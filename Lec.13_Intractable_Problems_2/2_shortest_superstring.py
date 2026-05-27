import sys
input = sys.stdin.readline

INF = float('inf')


def tsp_dp(n: int, W: list) -> int:
    # T(n) = O(n^2 * 2^n)
    # dp[mask][v]: 0번(dummy) 출발, mask에 속한 노드들을 방문하고 v에 있을 때 최소 비용
    # mask의 bit i → 노드 i+1 방문 여부 (노드 0은 dummy start이므로 마스크에서 제외)
    dp = [[INF] * n for _ in range(1 << (n - 1))]
    dp[0][0] = 0  # dummy start(0번)에서 출발, 비용 0

    for mask in range(1 << (n - 1)):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(1, n):
                if mask & (1 << (v - 1)):  # v 이미 방문 → 스킵
                    continue
                next_mask = mask | (1 << (v - 1))
                next_cost = dp[mask][u] + W[u][v]
                if next_cost < dp[next_mask][v]:
                    dp[next_mask][v] = next_cost

    # 모든 단어를 방문한 상태에서 최솟값 반환
    # TSP와 달리 출발점으로 복귀하지 않음 (Hamiltonian path)
    full = (1 << (n - 1)) - 1
    return min(dp[full][v] for v in range(1, n))


n = int(input())
words = [input().strip() for _ in range(n)]

# dummy start("")를 노드 0으로 추가 → 어떤 단어든 첫 번째로 선택 가능하게 함
nodes = [""] + words
m = len(nodes)  # = n + 1

# overlap[i][j]: nodes[i]의 접미사와 nodes[j]의 접두사가 겹치는 최대 길이
overlap = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        max_len = min(len(nodes[i]), len(nodes[j]))
        for k in range(max_len, 0, -1):
            if nodes[i][-k:] == nodes[j][:k]:
                overlap[i][j] = k
                break

# W[i][j]: i 다음에 j를 이어 붙일 때 추가되는 문자 수
# = len(nodes[j]) - overlap[i][j]  (겹치는 부분 제외)
W = [[INF] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        if i == j:
            W[i][j] = 0
        else:
            W[i][j] = len(nodes[j]) - overlap[i][j]

print(tsp_dp(m, W))
