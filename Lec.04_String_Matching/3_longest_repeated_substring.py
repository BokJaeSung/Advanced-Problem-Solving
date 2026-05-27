import sys
input = sys.stdin.readline

def has_duplicate(s, L, d=256, q=10**9+7):
    if L == 0:
        return True
    n = len(s)
    h = pow(d, L-1, q)
    t = 0
    for i in range(L):
        t = (d * t + ord(s[i])) % q
    seen = {t: [0]}
    for i in range(1, n - L + 1):
        t = (d * (t - ord(s[i-1]) * h) + ord(s[i+L-1])) % q
        if t in seen:
            for prev in seen[t]:
                if s[prev:prev+L] == s[i:i+L]:
                    return True
            seen[t].append(i)
        else:
            seen[t] = [i]
    return False

def longest_repeated(s):
    n = len(s)
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if has_duplicate(s, mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

s = input().strip()
print(longest_repeated(s))