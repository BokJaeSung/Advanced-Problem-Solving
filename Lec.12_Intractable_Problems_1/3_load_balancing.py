import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def load_balancing_branch_and_bound(n: int, k: int, jobs: list) -> int:
    jobs.sort(reverse=True)  # 큰 작업부터 배정 → 탐색 공간 조기 가지치기

    # suffix_sum[i]: jobs[i:] 의 합 → lower bound 계산에 사용
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + jobs[i]

    def lower_bound(i, loads):
        # 현재 최대 부하와 남은 작업을 k명이 완벽히 균등 분배한다고 가정한 값 중 큰 것
        # → 실제 최적값의 하한 (admissible)
        current_max = max(loads)
        remaining_sum = suffix_sum[i]
        total_sum = sum(loads) + remaining_sum
        average_bound = (total_sum + k - 1) // k  # ceil(total / k)
        return max(current_max, average_bound)

    def greedy_upper_bound():
        # 매 단계 부하가 가장 적은 일꾼에게 배정하는 greedy → 실현 가능한 상한
        # best_first_search의 초기 best 값으로 사용해 탐색 공간을 빠르게 좁힘
        loads = [0] * k
        for job in jobs:
            w = min(range(k), key=lambda x: loads[x])
            loads[w] += job
        return max(loads)

    def best_first_search():
        nonlocal best
        initial_loads = tuple([0] * k)
        PQ = []
        heappush(PQ, (lower_bound(0, initial_loads), 0, initial_loads))
        visited = set()
        visited.add((0, initial_loads))

        while PQ:
            lb, i, loads = heappop(PQ)

            if lb >= best:
                continue        # 현재 하한이 이미 best 이상 → 가지치기

            if i == n:
                best = min(best, max(loads))  # 모든 작업 배정 완료 → 갱신
                continue

            job = jobs[i]
            used = set()        # 동일 부하 일꾼에게 중복 배정 방지 (대칭 제거)
            for w in range(k):
                if loads[w] in used:
                    continue
                used.add(loads[w])

                new_loads = list(loads)
                new_loads[w] += job
                new_loads.sort()        # 정렬로 동치 상태 통합 → visited 효율 향상
                new_loads = tuple(new_loads)

                new_lb = lower_bound(i + 1, new_loads)
                if new_lb >= best:
                    continue    # 하한이 best 이상 → 가지치기

                state = (i + 1, new_loads)
                if state in visited:
                    continue
                visited.add(state)
                heappush(PQ, (new_lb, i + 1, new_loads))

    best = greedy_upper_bound()  # 초기 상한: greedy 해
    best_first_search()
    return best


n, k = map(int, input().split())
jobs = list(map(int, input().split()))

print(load_balancing_branch_and_bound(n, k, jobs))
