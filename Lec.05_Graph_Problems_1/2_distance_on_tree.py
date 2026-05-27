import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    
    # 트리 구성 (가중치 포함)
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    LOG = 17
    depth = [0] * (n + 1)
    dist = [0] * (n + 1)   # 루트에서 각 노드까지 가중치 합
    parent = [[0] * LOG for _ in range(n + 1)]
    
    # BFS로 depth, dist, parent[v][0] 채우기
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    while queue:
        v = queue.popleft()
        for u, w in graph[v]:
            if not visited[u]:
                visited[u] = True
                depth[u] = depth[v] + 1
                dist[u] = dist[v] + w    # 누적 가중치
                parent[u][0] = v
                queue.append(u)
    
    # DP로 나머지 채우기
    for k in range(1, LOG):
        for v in range(1, n + 1):
            parent[v][k] = parent[parent[v][k-1]][k-1]
    
    # LCA
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                u = parent[u][k]
        
        if u == v:
            return u
        
        for k in range(LOG - 1, -1, -1):
            if parent[u][k] != parent[v][k]:
                u = parent[u][k]
                v = parent[v][k]
        
        return parent[u][0]
    
    # 거리 = dist[u] + dist[v] - 2 * dist[LCA]
    def distance(u, v):
        l = lca(u, v)
        return dist[u] + dist[v] - 2 * dist[l]
    
    m = int(input())
    result = []
    for _ in range(m):
        u, v = map(int, input().split())
        result.append(distance(u, v))
    
    print('\n'.join(map(str, result)))

main()
