# 2-SAT (2-Satisfiability)
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve_2_SAT(n,scc_list):
    scc_id={}
    for id, scc in enumerate(scc_list):
        for u in scc:
            scc_id[u] = id
    for u in range(1,n+1):
        if scc_id[u]==scc_id[-u]:
            return False
        
    return True

def kosaraju(n,graph,Tgraph):
    visited =set()
    order =[]
    nodes= [id for id in range(-n,n+1) if id !=0]
    for u in nodes:
        if u not in visited:
            dfs_first(u,graph,visited,order)
    visited =set()
    scc_list=[]
    for u in reversed(order):
        if u not in visited:
            scc=[]
            dfs_second(u,Tgraph,visited,scc)
            scc_list.append(scc)
    return scc_list
    

def solve():
    n, m  = map(int, input().strip().split())
    graph = defaultdict(list)
    Tgraph= defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().strip().split())
        graph[-u].append(v)
        graph[-v].append(u)
        Tgraph[v].append(-u)
        Tgraph[u].append(-v)

    scc_list = kosaraju(n,graph,Tgraph)
    print(solve_2_SAT(n,scc_list))

solve()
