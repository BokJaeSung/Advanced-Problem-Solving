# PS.7.2: Minimum Cut
import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque


def bfs(graph, capacity, source,n, sink):
    queue = deque([(source,float('inf'))])
    parent = [-1] *(n+1)
    parent[source]=source
    while queue:
        u, flow =  queue.popleft()
        for v in graph[u]:
            if parent[v] == -1 and capacity[u][v]>0:
                parent[v]=u
                new_flow = min(flow,capacity[u][v])
                if v == sink:
                    return new_flow,parent
                queue.append((v,new_flow))
    return 0,None

def edmonds_karp(graph, capacity, source, sink, n):
    max_flow=0

    while True:
        flow, parent = bfs(graph, capacity, source, sink, n)
        if flow == 0 or parent is None:
            break
        max_flow += flow

        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= flow
            capacity[v][u] += flow
            v = u

    return max_flow


def find_cut(graph,capacity,source,n):
    queue=deque([source])
    visited=[False]*(n+1)
    visited[source]=True
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v] and capacity[u][v ]> 0:
                visited[v] = True
                queue.append(v)
    S = [v for v in range(1, n + 1) if visited[v]]
    T = [v for v in range(1, n + 1) if not visited[v]]
    return S,T

def solve():
    n, m = map(int, input().split())

    capacity = [[0] * (n + 1) for _ in range(n + 1)]
    graph = defaultdict(list)
    for _ in range(m):
        u, v ,cap= map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        capacity[u][v] +=cap
    print(edmonds_karp(graph, capacity, source=1, sink=n, n=n))
    S,T= find_cut(graph,capacity,source=1,n=n)
    print(*sorted(S))
    print(*sorted(T))
solve()