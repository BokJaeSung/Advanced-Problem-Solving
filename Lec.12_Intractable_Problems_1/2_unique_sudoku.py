import sys
input = sys.stdin.readline

# bit 1~9를 사용: FULL = 0b1111111110 (bit 1~9 모두 켜짐)
FULL = (1 << 10) - 2
count = 0


def find_best_cell(grid, row_mask, col_mask, box_mask):
    # MRV(Minimum Remaining Values): 후보 숫자가 가장 적은 빈 칸 선택
    # → 가지치기 효율 극대화
    best_cell = None
    best_mask = 0
    best_count = 10
    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                continue
            b = (r // 3) * 3 + (c // 3)
            # 이 칸에 놓을 수 있는 숫자 후보 마스크
            mask = FULL & ~(row_mask[r] | col_mask[c] | box_mask[b])
            cnt = bin(mask).count('1')
            if cnt == 0:
                return (r, c), 0   # 후보 없음 → 즉시 실패 반환
            if cnt < best_count:
                best_cell, best_mask, best_count = (r, c), mask, cnt
            if cnt == 1:
                return best_cell, best_mask  # 후보 1개 → 즉시 확정
    return best_cell, best_mask


def backtrack(grid, row_mask, col_mask, box_mask):
    global count
    cell, mask = find_best_cell(grid, row_mask, col_mask, box_mask)
    if cell is None:
        count += 1  # 솔루션 하나 발견
        return
    if mask == 0:
        return      # 후보 없음 → 백트래킹

    r, c = cell
    b = (r // 3) * 3 + (c // 3)

    while mask:
        bit = mask & -mask          # 최하위 1비트 추출
        x = bit.bit_length() - 1   # 비트 위치 → 실제 숫자
        grid[r][c] = x
        row_mask[r] |= bit
        col_mask[c] |= bit
        box_mask[b] |= bit

        backtrack(grid, row_mask, col_mask, box_mask)

        # 백트래킹: 배치 취소
        grid[r][c] = 0
        row_mask[r] ^= bit
        col_mask[c] ^= bit
        box_mask[b] ^= bit

        if count >= 2:
            return  # 솔루션이 2개 이상 확인됨 → 더 탐색 불필요

        mask &= mask - 1            # 처리한 최하위 비트 제거


def init_masks(grid):
    row_mask = [0] * 9
    col_mask = [0] * 9
    box_mask = [0] * 9
    for r in range(9):
        for c in range(9):
            x = grid[r][c]
            if x == 0:
                continue
            bit = 1 << x
            b = (r // 3) * 3 + (c // 3)
            row_mask[r] |= bit
            col_mask[c] |= bit
            box_mask[b] |= bit
    return row_mask, col_mask, box_mask


grid = [list(map(int, input().split())) for _ in range(9)]
row_mask, col_mask, box_mask = init_masks(grid)
backtrack(grid, row_mask, col_mask, box_mask)

print("YES" if count == 1 else "NO")
