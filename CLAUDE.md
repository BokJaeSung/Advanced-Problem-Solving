# Advanced Problem Solving — CLAUDE.md

## File & Directory Naming Rules

### Directory format
```
Lec.{번호}_{Topic_Name}_{번호(복수 파트일 때)}
```
- 번호는 두 자리 없이 그대로 (Lec.01, Lec.12 등)
- 토픽 단어는 `_`로 연결, 각 단어 첫 글자 대문자
- 복수 파트는 끝에 `_1`, `_2`, `_3` 붙임

예시:
```
Lec.10_Optimization_Problems_2/
Lec.11_Optimization_Problems_3/
Lec.12_Intractable_Problems_1/
```

### File format
```
{번호}_{problem_name_snake_case}.py
```
- 번호는 1부터 순서대로
- 문제 이름은 소문자 snake_case

예시:
```
1_minimum_vertex_cover.py
2_minimum_set_cover.py
1_sudoku_puzzle.py
2_unique_sudoku.py
3_load_balancing.py
```

## Code Conventions

- 파일 상단: `import sys` / `input = sys.stdin.readline`
- `bit_count()` 대신 `popcount(x) = bin(x).count('1')` 사용 (Python 3.9 이하 호환)
- brute-force / greedy 분기 기준은 문제 조건에 따름
- 주석: 핵심 로직의 WHY 위주로 작성
