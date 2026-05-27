import sys
sys.setrecursionlimit(20000)

MATCH, SUBST, INS, DEL = 0, 1, 2, 3


def solve():
    X = input().strip()
    Y = input().strip()

    m, n = len(X), len(Y)
    X1 = "_" + X  # 1-based indexing
    Y1 = "_" + Y

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    path = [[None] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(1, m + 1):
        dp[i][0] = i
        path[i][0] = DEL
    for j in range(1, n + 1):
        dp[0][j] = j
        path[0][j] = INS

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            substitution_cost = 0 if X1[i] == Y1[j] else 1
            operation = MATCH if X1[i] == Y1[j] else SUBST
            # Tie-breaking order: MATCH/SUBST > DEL > INS
            candidates = [
                (dp[i - 1][j - 1] + substitution_cost, operation),
                (dp[i - 1][j] + 1, DEL),
                (dp[i][j - 1] + 1, INS),
            ]
            dp[i][j], path[i][j] = min(candidates, key=lambda x: x[0])

    # Reconstruct path iteratively (avoid deep recursion)
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i == 0:
            operations.append((INS, i, Y1[j]))
            j -= 1
        elif j == 0:
            operations.append((DEL, i, X1[i]))
            i -= 1
        else:
            p = path[i][j]
            if p == MATCH:
                i -= 1
                j -= 1
            elif p == SUBST:
                operations.append((SUBST, i, Y1[j]))
                i -= 1
                j -= 1
            elif p == INS:
                operations.append((INS, i, Y1[j]))
                j -= 1
            elif p == DEL:
                operations.append((DEL, i, X1[i]))
                i -= 1

    operations.reverse()

    out = [str(dp[m][n])]
    for op, idx, c in operations:
        if op == INS:
            out.append(f"INSERT {idx} {c}")
        elif op == DEL:
            out.append(f"DELETE {idx} {c}")
        elif op == SUBST:
            out.append(f"SUBST {idx} {c}")
    print("\n".join(out))


solve()