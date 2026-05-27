import sys
input = sys.stdin.readline
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])

    # 트리 크기를 2n으로 설정하여 메모리 절약
    tree = [0] * (2 * n)

    # 리프 노드 채우기
    for i in range(n):
        tree[n + i] = arr[i]

    # 내부 노드 채우기 (비트 연산 및 단순 조건문으로 속도 최적화)
    for i in range(n - 1, 0, -1):
        left_child = tree[i << 1]
        right_child = tree[i << 1 | 1]
        tree[i] = left_child if left_child < right_child else right_child

    idx = n + 2
    results = []
    
    for _ in range(m):
        # 쿼리 구간을 트리의 리프 노드 인덱스에 맞게 조정
        left = int(input_data[idx]) + n
        right = int(input_data[idx+1]) + n + 1
        idx += 2
        
        min_val = sys.maxsize

        # 바텀업 방식으로 부모 노드로 이동하며 구간 최솟값 탐색
        while left < right:
            if left % 2 == 1:
                if tree[left] < min_val:
                    min_val = tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                if tree[right] < min_val:
                    min_val = tree[right]
            
            # 비트 시프트 연산으로 2로 나누는 작업 대체
            left >>= 1
            right >>= 1
        
        results.append(str(min_val))

    # 결과를 모아서 한 번에 출력 (작은 따옴표 사용)
    print('\n'.join(results))

if __name__ == '__main__':
    solve()