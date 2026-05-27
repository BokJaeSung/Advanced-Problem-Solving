# Lec.12 Intractable Problems (1) — 빈칸 예상문제

---

## PS.12.1 / PS.12.2 — Sudoku (Backtracking + MRV)

### Q1. FULL 마스크 값

비트 1~9를 사용 가능 숫자로 표현할 때 `FULL`의 값은?

```python
FULL = ______
```

<details><summary>정답</summary>

```python
FULL = (1 << 10) - 2  # 0b1111111110 (bit 1~9 켜짐, bit 0 꺼짐)
```

</details>

---

### Q2. 후보 숫자 마스크 계산

칸 `(r, c)`에 놓을 수 있는 숫자 후보 마스크를 구하는 식은?

```python
b = (r // 3) * 3 + (c // 3)
mask = ______
```

<details><summary>정답</summary>

```python
mask = FULL & ~(row_mask[r] | col_mask[c] | box_mask[b])
```

행·열·박스에서 이미 사용된 비트를 전부 OR한 뒤 반전(`~`)하여 FULL과 AND → 아직 사용 안 된 숫자만 남긴다.

</details>

---

### Q3. MRV — 즉시 실패 반환 조건

후보가 0개인 칸을 발견했을 때 즉시 반환해야 하는 이유와 반환값은?

```python
cnt = bin(mask).count('1')
if cnt == 0:
    return ______, ______
```

<details><summary>정답</summary>

```python
return (r, c), 0
```

후보가 없으면 이 분기는 반드시 실패 → 더 탐색할 필요 없이 즉시 실패 신호를 전달한다.

</details>

---

### Q4. 최하위 1비트 추출 및 숫자 변환

마스크에서 후보 숫자를 하나씩 꺼내는 두 줄은?

```python
while mask:
    bit = ______
    x   = ______
```

<details><summary>정답</summary>

```python
bit = mask & -mask          # 최하위 1비트만 추출 (-mask = ~mask + 1)
x   = bit.bit_length() - 1  # 비트 위치 → 실제 숫자 (bit 3 → x=3)
```

</details>

---

### Q5. 비트마스크 배치 및 취소 (백트래킹)

숫자 `x`를 `(r,c)`에 배치할 때와 되돌릴 때의 마스크 연산은?

```python
# 배치
row_mask[r] ______ bit
col_mask[c] ______ bit
box_mask[b] ______ bit

# 취소 (백트래킹)
row_mask[r] ______ bit
col_mask[c] ______ bit
box_mask[b] ______ bit
```

<details><summary>정답</summary>

```python
# 배치
row_mask[r] |= bit   # OR: 해당 비트 켜기
col_mask[c] |= bit
box_mask[b] |= bit

# 취소
row_mask[r] ^= bit   # XOR: 켜진 비트만 끄기 (배치된 상태에서만 사용)
col_mask[c] ^= bit
box_mask[b] ^= bit
```

</details>

---

### Q6. 처리한 비트 제거

`while mask` 루프에서 현재 bit를 처리한 뒤 마스크에서 제거하는 식은?

```python
mask = ______
```

<details><summary>정답</summary>

```python
mask &= mask - 1   # 최하위 1비트 제거
```

`mask - 1`은 최하위 1비트를 0으로, 그 아래 모든 비트를 1로 바꾼다. AND하면 해당 비트만 제거된다.

</details>

---

### Q7. PS.12.1 vs PS.12.2 — backtrack 차이

두 문제에서 `backtrack` 함수의 핵심 차이점 두 가지는?

<details><summary>정답</summary>

| 항목 | PS.12.1 (풀이 출력) | PS.12.2 (유일성 판별) |
|---|---|---|
| 반환값 | `True/False` (첫 솔루션 즉시 종료) | 없음 (전체 탐색) |
| 완료 처리 | `return True` | `count += 1` |
| 조기 종료 | 솔루션 1개 발견 시 | `count >= 2` 시 |

</details>

---

## PS.12.3 — Load Balancing (Branch & Bound)

### Q8. suffix_sum 초기화

`suffix_sum[i]` = `jobs[i:]`의 합을 뒤에서부터 채우는 코드는?

```python
suffix_sum = [0] * (n + 1)
for i in range(______, ______):
    suffix_sum[i] = ______
```

<details><summary>정답</summary>

```python
for i in range(n - 1, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + jobs[i]
```

</details>

---

### Q9. lower_bound 계산

`lower_bound(i, loads)`에서 두 가지 하한을 구하고 그 중 큰 값을 반환하는 식은?

```python
current_max   = ______
average_bound = ______          # ceil(전체합 / k)
return ______
```

<details><summary>정답</summary>

```python
current_max   = max(loads)
total_sum     = sum(loads) + suffix_sum[i]
average_bound = (total_sum + k - 1) // k   # 정수 올림나눗셈
return max(current_max, average_bound)
```

- `current_max`: 이미 배정된 부하의 최댓값 → 줄일 수 없는 하한
- `average_bound`: 남은 작업을 완벽히 균등 분배해도 이만큼은 필요 → 이상적 하한

</details>

---

### Q10. greedy_upper_bound

매 단계 부하가 가장 적은 일꾼에게 배정하는 greedy 한 줄은?

```python
for job in jobs:
    w = ______
    loads[w] += job
```

<details><summary>정답</summary>

```python
w = min(range(k), key=lambda x: loads[x])
```

</details>

---

### Q11. 대칭 가지치기 (중복 배정 방지)

동일한 부하를 가진 일꾼에게 중복으로 배정하는 경우를 제거하는 코드는?

```python
used = set()
for w in range(k):
    if ______:
        continue
    used.add(______)
```

<details><summary>정답</summary>

```python
used = set()
for w in range(k):
    if loads[w] in used:   # 이미 같은 부하의 일꾼에게 배정 시도했음
        continue
    used.add(loads[w])
```

부하가 같은 일꾼끼리는 배정 결과가 동일 → 하나만 탐색하면 충분.

</details>

---

### Q12. 동치 상태 통합

서로 다른 배정 순서가 같은 상태임을 visited로 감지하기 위해 `new_loads`에 하는 처리는?

```python
new_loads = list(loads)
new_loads[w] += job
______          # 동치 상태 통합
new_loads = tuple(new_loads)
```

<details><summary>정답</summary>

```python
new_loads.sort()
```

일꾼의 부하를 정렬하면 배정 순서가 달라도 동일한 tuple이 되어 visited로 중복을 제거할 수 있다.

</details>

---

### Q13. Branch & Bound 가지치기 조건

PQ에서 꺼낸 노드와 자식 노드를 각각 가지치기하는 조건은?

```python
# 현재 노드
if ______:
    continue

# 자식 노드 생성 후
if ______:
    continue
```

<details><summary>정답</summary>

```python
# 현재 노드: 하한이 이미 best 이상이면 탐색 불필요
if lb >= best:
    continue

# 자식 노드: 자식의 하한도 best 이상이면 추가 안 함
if new_lb >= best:
    continue
```

`>=` 를 사용하는 이유: best와 같아도 더 나은 해를 찾을 수 없으므로 탐색 불필요.

</details>

---

### Q14. Branch & Bound 전체 흐름 순서

`load_balancing_branch_and_bound` 함수의 실행 순서를 채우시오.

```
1. jobs를 ______ 순으로 정렬
2. ______ 배열 초기화 (하한 계산용)
3. best = ______ (초기 상한)
4. best_first_search() 실행
   - PQ에서 lb가 가장 작은 상태 추출
   - lb >= best 이면 ______
   - i == n 이면 ______
   - 아니면 job을 각 일꾼에게 배정 → ______ 가지치기 후 PQ 삽입
5. best 반환
```

<details><summary>정답</summary>

```
1. 내림차순(reverse=True)
2. suffix_sum
3. greedy_upper_bound()
4. - 가지치기(continue)
   - best 갱신(best = min(best, max(loads)))
   - 대칭 제거 + lower_bound
```

</details>
