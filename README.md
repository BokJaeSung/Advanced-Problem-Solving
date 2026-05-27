# Advanced Problem Solving

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Problems](https://img.shields.io/badge/Problems-18-brightgreen?style=flat)
![Topics](https://img.shields.io/badge/Topics-Graph%20%7C%20Optimization%20%7C%20Intractable-blueviolet?style=flat)

A collection of advanced algorithm implementations in Python, based on the following references:

- T. Cormen et al., *Introduction to Algorithms*, 3rd Ed. (CLRS)
- S. Skiena, *The Algorithm Design Manual*, 3rd Ed.
- S. Halim & F. Halim, *Competitive Programming*
- A. Laaksonen, *Competitive Programmer's Handbook*

---

## 🔵 Graph Problems

| Lec | Topic | Problems | Key Algorithms |
|-----|-------|----------|----------------|
| [`Lec.05`](Lec.05_Graph_Problems_1/) | Graph Problems (1) | [LCA](Lec.05_Graph_Problems_1/1_lowest_common_ancestor.py) · [Distance on Tree](Lec.05_Graph_Problems_1/2_distance_on_tree.py) · [RMQ](Lec.05_Graph_Problems_1/3_range_minimum_query.py) | LCA, Sparse Table |
| [`Lec.06`](Lec.06_Graph_Problems_2/) | Graph Problems (2) | [Kosaraju](Lec.06_Graph_Problems_2/1_kosaraju.py) · [Tarjan](Lec.06_Graph_Problems_2/2_tarjan.py) · [Min Source Cover](Lec.06_Graph_Problems_2/3_minimum_source_cover.py) · [2-SAT](Lec.06_Graph_Problems_2/4_two_sat.py) | SCC, 2-SAT |
| [`Lec.07`](Lec.07_Graph_Problems_3/) | Graph Problems (3) | [Edge-Disjoint Paths](Lec.07_Graph_Problems_3/1_edge_disjoint_paths.py) · [Min Cut](Lec.07_Graph_Problems_3/2_minimum_cut.py) · [Bipartite Matching](Lec.07_Graph_Problems_3/3_bipartite_matching.py) | Ford-Fulkerson, Max-Flow Min-Cut |

---

## 🟠 Optimization Problems

| Lec | Topic | Problems | Key Algorithms |
|-----|-------|----------|----------------|
| [`Lec.09`](Lec.09_Optimization_Problems_1/) | Optimization Problems (1) | — | Divide & Conquer Opt, Knuth's Opt |
| [`Lec.10`](Lec.10_Optimization_Problems_2/) | Optimization Problems (2) | [SSSP](Lec.10_Optimization_Problems_2/1_single_source_shortest_paths.py) · [SSSP (Negative)](Lec.10_Optimization_Problems_2/2_sssp_with_negative_edges.py) · [Sliding Puzzle](Lec.10_Optimization_Problems_2/3_sliding_puzzles.py) | Dijkstra, Bellman-Ford, A\* |
| [`Lec.11`](Lec.11_Optimization_Problems_3/) | Optimization Problems (3) | [Min Vertex Cover](Lec.11_Optimization_Problems_3/1_minimum_vertex_cover.py) · [Min Set Cover](Lec.11_Optimization_Problems_3/2_minimum_set_cover.py) | Brute-Force, Greedy Approximation |

---

## 🔴 Intractable Problems

| Lec | Topic | Problems | Key Algorithms |
|-----|-------|----------|----------------|
| [`Lec.12`](Lec.12_Intractable_Problems_1/) | Intractable Problems (1) | [Sudoku Puzzle](Lec.12_Intractable_Problems_1/1_sudoku_puzzle.py) · [Unique Sudoku](Lec.12_Intractable_Problems_1/2_unique_sudoku.py) · [Load Balancing](Lec.12_Intractable_Problems_1/3_load_balancing.py) | Backtracking (MRV), Branch & Bound |
| [`Lec.13`](Lec.13_Intractable_Problems_2/) | Intractable Problems (2) | [TSP](Lec.13_Intractable_Problems_2/1_traveling_salesperson_problem.py) · [Shortest Superstring](Lec.13_Intractable_Problems_2/2_shortest_superstring.py) · [Euclidean TSP](Lec.13_Intractable_Problems_2/3_euclidean_tsp.py) | Held-Karp DP, MST Heuristic |

---

## 📚 Early Lectures

| Lec | Topic | Problems | Key Algorithms |
|-----|-------|----------|----------------|
| [`Lec.01`](Lec.01_Introduction/) | Introduction | — | — |
| [`Lec.02`](Lec.02_Numerical_Problems/) | Numerical Problems | — | — |
| [`Lec.03`](Lec.03_Geometric_Problems/) | Geometric Problems | — | — |
| [`Lec.04`](Lec.04_String_Matching/) | String Matching | [Pattern Matching](Lec.04_String_Matching/1_string_pattern_matching.py) · [String Exponentiation](Lec.04_String_Matching/2_string_exponentiation.py) · [Longest Repeated Substring](Lec.04_String_Matching/3_longest_repeated_substring.py) | KMP, Z-algorithm, Suffix Array |
