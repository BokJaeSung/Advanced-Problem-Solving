
import sys
input = sys.stdin.readline

def count_inversions(state: str) -> int:
    # 빈칸('0')을 제외한 타일 번호를 16진수 → 정수로 변환
    # 예: '1', '2', 'A'(=10), 'F'(=15) 등
    arr = [int(c, base=16) for c in state if c != '0']
    cnt = 0
    # 모든 (i, j) 쌍에서 arr[i] > arr[j] 인 경우 = inversion(역전) 개수 세기
    # inversion: 앞에 있는 수가 뒤에 있는 수보다 큰 경우 (정렬 기준 위반)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            cnt += arr[i] > arr[j]
    return cnt

def solvable(n: int, state: str) -> bool:
    inv = count_inversions(state)
    if n % 2 == 1:  # 보드 너비가 홀수인 경우 (3x3, 5x5 등)
        # inversion 수가 짝수면 풀 수 있음
        return inv % 2 == 0
    else:  # 보드 너비가 짝수인 경우 (4x4 등)
        blank = state.index('0')
        # 빈칸이 위에서 몇 번째 행인지 (1-indexed, 아래에서 세기)
        row = n - blank // n
        # inversion 수 + 빈칸 행 번호의 홀짝이 홀수면 풀 수 있음
        return (inv + row) % 2 == 1

# A* 휴리스틱: 각 타일의 맨해튼 거리 합 (admissible: 실제 이동 수를 절대 과대추정 안 함)
def h(n: int, state: str) -> int:
    dist = 0
    for idx, tile in enumerate(state):
        if tile == '0':
            continue  # 빈칸은 무시
        goal = int(tile, base=16) - 1  # 이 타일이 목표 상태에서 있어야 할 인덱스
        r, c = divmod(idx, n)          # 현재 위치 (행, 열)
        rstar, cstar = divmod(goal, n) # 목표 위치 (행, 열)
        dist += abs(r - rstar) + abs(c - cstar)  # 맨해튼 거리
    return dist

from heapq import heappush, heappop

def move(state, blank, di, dj, n):
    r, c = divmod(blank, n)   # 빈칸의 현재 (행, 열)
    nr, nc = r + di, c + dj  # 이동 후 (행, 열)

    # 보드 밖으로 나가면 이동 불가
    if not (0 <= nr < n and 0 <= nc < n):
        return None

    nxt = nr * n + nc  # 이동할 위치의 1D 인덱스
    arr = list(state)
    arr[blank], arr[nxt] = arr[nxt], arr[blank]  # 빈칸과 타일 교환

    return "".join(arr)  # 새로운 상태 문자열 반환

def a_star_search(n: int, start: str) -> int:
    # 목표 상태: "123...0" (빈칸이 맨 마지막)
    # n=4이면 "123456789ABCDEF0"
    target = "123456789ABCDEF"[:n*n-1] + "0"

    if start == target:
        return 0  # 이미 목표 상태

    # 힙: (f=g+h, g=이동횟수, state=현재 보드 상태)
    PQ = [(h(n, start), 0, start)]
    # g[state]: 해당 상태까지의 최소 이동 횟수
    g = {start: 0}

    while PQ:
        f, depth, state = heappop(PQ)

        # 힙에서 꺼냈는데 이미 더 짧은 경로로 처리된 상태면 스킵
        # (다익스트라의 중복 방문 처리와 동일한 원리)
        if depth != g[state]:
            continue

        if state == target:
            return depth  # 목표 도달 → 최소 이동 횟수 반환

        blank = state.index('0')  # 현재 빈칸 위치

        # 상하좌우 4방향으로 빈칸 이동 시도
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_state = move(state, blank, di, dj, n)
            if new_state is None:
                continue  # 보드 밖 = 이동 불가

            new_depth = depth + 1  # 이동 1회 추가

            # 이 상태를 처음 보거나, 더 짧은 경로를 발견한 경우에만 갱신
            if new_state not in g or new_depth < g[new_state]:
                g[new_state] = new_depth
                new_f = g[new_state] + h(n, new_state)  # f = g + h
                heappush(PQ, (new_f, new_depth, new_state))

    return -1  # 목표에 도달 불가 (solvable 검사 후 호출되므로 사실상 도달 안 함)


# ── 입력 ──────────────────────────────────────────────
n = int(input())
# n줄 입력을 공백 제거 후 이어 붙여 하나의 문자열로 만들기
# 예: "1 2 3\n4 5 6\n7 8 0" → "123456780"
state = "".join("".join(input().split()) for _ in range(n))

if not solvable(n, state):
    print(-1)  # 풀 수 없는 초기 상태
else:
    print(a_star_search(n, state))  # 최소 이동 횟수 출력