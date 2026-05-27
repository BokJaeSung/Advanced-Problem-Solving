import sys
input = sys.stdin.readline
import sys
input = sys.stdin.readline

def compute_pi(s):
    m = len(s)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and s[k] != s[q]:
            k = pi[k-1]
        if s[k] == s[q]:
            k += 1
        pi[q] = k
    return pi

def maximum_exponent(s):
    n = len(s)
    pi = compute_pi(s)
    period = n - pi[-1]
    if n % period == 0:
        return n // period
    else:
        return 1

n = int(input())
for _ in range(n):
    s = input().strip()
    print(maximum_exponent(s))