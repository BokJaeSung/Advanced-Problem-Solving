import sys
sys.setrecursionlimit(20000)

MATCH, SUBST, INS, DEL = 0, 1, 2, 3

def edit_distance_tabulation(X: str, Y: str):
    m, n = len(X), len(Y)
    X, Y = "_" + X, "_" + Y          # 1-based indexing

    dp   = [[None] * (n + 1) for _ in range(m + 1)]
    path = [[None] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = 0
    for i in range(1, m + 1):
        dp[i][0] = i;  path[i][0] = DEL
    for j in range(1, n + 1):
        dp[0][j] = j;  path[0][j] = INS

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            substitution_cost = 0 if X[i] == Y[j] else 1
            operation         = MATCH if X[i] == Y[j] else SUBST
            candidates = [
                (dp[i-1][j-1] + substitution_cost, operation),  # ↖ match/subst
                (dp[i-1][j]   + 1,                 DEL),        # ↑  delete
                (dp[i][j-1]   + 1,                 INS),        # ←  insert
            ]
            dp[i][j], path[i][j] = min(candidates, key=lambda x: x[0])

    def reconstruct(i, j):
        if i == 0 and j == 0:
            return []
        elif i == 0:
            return reconstruct(i, j - 1) + [(INS,   i, Y[j])]
        elif j == 0:
            return reconstruct(i - 1, j) + [(DEL,   i, X[i])]
        if   path[i][j] == MATCH:
            return reconstruct(i - 1, j - 1) + [(MATCH, i, X[i])]
        elif path[i][j] == SUBST:
            return reconstruct(i - 1, j - 1) + [(SUBST, i, Y[j])]
        elif path[i][j] == INS:
            return reconstruct(i,     j - 1) + [(INS,   i, Y[j])]
        elif path[i][j] == DEL:
            return reconstruct(i - 1, j    ) + [(DEL,   i, X[i])]

    return dp[m][n], reconstruct(m, n)


def solve():
    X = input().strip()
    Y = input().strip()

    dist, ops = edit_distance_tabulation(X, Y)

    # x_pos: 현재 X 문자열에서 다음 처리할 위치 (삽입/삭제로 변하는 실제 위치)
    result = []
    x_pos  = 1
    for op_type, _, char in ops:
        if   op_type == MATCH:
            x_pos += 1
        elif op_type == SUBST:
            result.append(f"SUBST {x_pos} {char}")
            x_pos += 1
        elif op_type == INS:
            result.append(f"INSERT {x_pos} {char}")
            x_pos += 1
        elif op_type == DEL:
            result.append(f"DELETE {x_pos} {char}")
            # x_pos 유지: 삭제 후 다음 문자가 같은 자리로 당겨짐

    print(dist)
    for r in result:
        print(r)

solve()