import sys
input = sys.stdin.readline


def to_mask(S):
    # 원소 집합 S를 비트마스크로 변환 (원소 x → bit x-1)
    # 예: {1,3,5} → 0b10101 = 21
    mask = 0
    for x in S:
        mask |= 1 << (x - 1)
    return mask


def popcount(x):
    # bin(x) = '0b101...' 형태의 문자열 → '1'의 개수 = 켜진 비트 수
    return bin(x).count('1')


def is_set_cover(mask, masks, full):
    # mask의 각 비트가 F의 부분집합 포함 여부를 나타냄 (bit i → F[i])
    covered = 0
    for i in range(len(masks)):
        if mask & (1 << i):         # i번째 부분집합이 선택됐으면
            covered |= masks[i]     # 해당 집합의 원소를 covered에 합산
    return covered == full          # 전체 집합 X를 모두 커버하면 True


def min_set_cover_bruteforce(n: int, m: int, masks: list) -> list:
    # T(n, m) = O(2^m * m)
    # F의 모든 부분집합을 비트마스크로 열거 (0 ~ 2^m - 1)
    full = (1 << n) - 1         # 전체 집합 X를 비트마스크로 표현
    best = (1 << m) - 1         # 초기값: F의 모든 부분집합 선택
    for mask in range(1 << m):
        if is_set_cover(mask, masks, full):
            # 현재 cover 크기가 지금까지 최솟값보다 작으면 갱신
            if popcount(mask) < popcount(best):
                best = mask
    # best 마스크에서 켜진 비트 위치 → 선택된 부분집합 번호 (1-indexed)
    return [x for x in range(1, m + 1) if best & (1 << (x - 1))]


def argmax(masks: list, covered: int) -> int:
    # 아직 커버되지 않은 원소(~covered)를 가장 많이 포함하는 집합의 인덱스 반환
    best = -1
    best_new_cover = 0
    for i in range(len(masks)):
        new_cover = masks[i] & ~covered         # i번째 집합이 새로 커버하는 원소
        if popcount(new_cover) > best_new_cover:
            best = i
            best_new_cover = popcount(new_cover)
    return best


def min_set_cover_greedy(n: int, m: int, masks: list) -> list:
    # T(n, m) = O(n * m)
    # ln(n)+1 approximation: 최적해의 ln(n)+1배 이하 크기를 보장
    full = (1 << n) - 1  # 전체 집합 X
    covered = 0          # 현재까지 커버된 원소 집합 (비트마스크)
    selected = 0         # 선택된 부분집합 집합 (비트마스크)
    while covered != full:
        # 매 단계마다 새로 커버하는 원소가 가장 많은 집합 선택
        best = argmax(masks, covered)
        if best == -1 or (masks[best] & ~covered) == 0:
            return []   # 전체 집합을 커버할 수 없는 경우
        selected |= 1 << best
        covered |= masks[best]
    return [x for x in range(1, m + 1) if selected & (1 << (x - 1))]


n, m = map(int, input().split())
sets = [tuple(map(int, input().split())) for _ in range(m)]
masks = [to_mask(S) for S in sets]

if m < 16:
    # m < 16: brute-force로 정확한 최솟값 탐색
    C = min_set_cover_bruteforce(n, m, masks)
else:
    # m >= 16: greedy approximation (최적해의 ln(n)+1배 이하 보장)
    C = min_set_cover_greedy(n, m, masks)

print(len(C))
for i in C:
    print(*sets[i - 1])
