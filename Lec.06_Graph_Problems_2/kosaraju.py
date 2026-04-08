# Kosaraju's Algorithm - Strongly Connected Components (SCC)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict

def dfs_first(u,graph,visited,order):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs_first(v,graph,visited,order)
    order.append(u)

def dfs_second(u,Tgraph,visited,scc):
    visited.add(u)
    scc.append(u)
    for v in Tgraph[u]:
        if v not in visited:
            dfs_second(v,Tgraph,visited,scc)

def kosaraju(n, graph, Tgraph):
    visited =set()
    order = []
    for u in range(1,n+1):
        if u not in visited:
            dfs_first(u,graph,visited,order)

    order.reverse()
    
    visited =set()
    scc_list = []

    for u in order:
        if u not in visited:
            scc=[]
            dfs_second(u,Tgraph,visited,scc)
            scc_list.append(scc)
    return scc_list


def solve():
    n, m = map(int,input().strip().split())
    graph = defaultdict(list)
    Tgraph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        Tgraph[v].append(u)
    scc_list = kosaraju(n, graph, Tgraph)
    print(len(scc_list))
    for scc in scc_list:
        scc.sort()
    for scc in sorted(scc_list):
        print(*scc)
solve()
