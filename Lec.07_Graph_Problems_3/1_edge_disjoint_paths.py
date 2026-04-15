# PS.7.1: Edge-Disjoint Paths
import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

def bfs(graph, capacity, source, sink, n):
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


def solve():
    n, m = map(int, input().split())

    capacity = [[0] * (n + 1) for _ in range(n + 1)]
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        capacity[u][v] = 1
    print(edmonds_karp(graph, capacity, source=1, sink=n, n=n))

solve()
