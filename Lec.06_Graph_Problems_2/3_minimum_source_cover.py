# Problem 6.2: Minimum Source Cover
def count_indegree_zero(scc_list: list, graph :list) -> int:
    scc_id = {}
    for id , scc in enumerate(scc_list):
        for u in scc:
            scc_id[u]=id
    indegree = [0] * len(scc_list)
    for u in graph: # or scc_id
        for v in graph[u]:
            if scc_id[u]!=scc_id[v]:
                indegree[scc_id[v]]+=1
    return sum(d==0 for d in indegree)