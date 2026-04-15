# PS.7.3: Bipartite Matching
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
        flow, parent = bfs(graph, capacity, source, n, sink)
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

 

def find_matching(capacity, edges):
    matching = []
    for u, v in edges:
        if capacity[u][v] == 0:
            matching.append((u, v))
    return matching

def solve():
    L, R, m = map(int, input().split())
    n = L + R + 2
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    capacity = [[0] * (n ) for _ in range(n )]
    graph = defaultdict(list)
    s, t = 0 ,L+R+1

    for u in range(1,L+1):
        graph[s].append(u)
        graph[u].append(s) # backward edge for flow cancellation
        capacity[s][u] = 1

    for v in range(L+1,L+R+1):
        graph[v].append(t)
        graph[t].append(v) # backward edge for flow cancellation
        capacity[v][t] = 1

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        capacity[u][v] = 1

    print(edmonds_karp(graph, capacity, source=s, sink=t,n=n))
    matching = find_matching(capacity, edges)
    for u, v in matching:
        print(u, v)
solve()