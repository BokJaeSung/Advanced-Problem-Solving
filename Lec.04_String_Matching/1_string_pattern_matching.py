import sys
input = sys.stdin.readline

def compute_pi(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k-1]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    return pi

def kmp(T, P):
    n, m = len(T), len(P)
    pi = compute_pi(P)
    shifts = []
    q = 0
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q-1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            shifts.append(i - m + 1)  # shift값
            q = pi[q-1]
    return shifts

T = input().strip()
P = input().strip()

result = kmp(T, P)

print(len(result))
if result:
    print(*result)