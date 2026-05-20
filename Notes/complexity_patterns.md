# Complexity and Pattern Quick Reference

Print this. Keep it next to you during practice.

---

## Recognising Patterns from Problem Statement

| Keywords in problem | Pattern to use |
|--------------------|----------------|
| "two numbers that sum to" | Hash Map |
| "sorted array" + "find pair" | Two Pointers |
| "subarray" + "sum" or "length" | Sliding Window |
| "sorted" + "O(log n)" | Binary Search |
| "all subsets" or "all combinations" | Backtracking |
| "shortest path" unweighted | BFS |
| "shortest path" weighted | Dijkstra |
| "minimum cost" or "minimum steps" | DP or BFS |
| "number of ways" | DP |
| "maximum profit" or "minimum loss" | DP or Greedy |
| "level order" or "layer by layer" | BFS |
| "validate" a tree | DFS |
| "linked list" + "cycle" | Fast and Slow Pointers |
| "parentheses" or "brackets" | Stack |
| "next greater element" | Monotonic Stack |
| "top K" or "K largest" | Heap |
| "prefix sum" | Hash Map + Running Sum |

---

## Time Complexity by Input Size

When n is the input size and you have X seconds:

| Input size n | Maximum O(...) you can afford |
|---|---|
| n ≤ 10 | O(n!) — backtracking, permutations |
| n ≤ 20 | O(2^n) — bitmask DP |
| n ≤ 100 | O(n^3) — Floyd-Warshall, matrix chain |
| n ≤ 1,000 | O(n^2) — DP, bubble sort |
| n ≤ 100,000 | O(n log n) — sorting, heap, segment tree |
| n ≤ 1,000,000 | O(n) — hash map, two pointers, sliding window |
| n ≤ 10^9 | O(log n) — binary search, fast exponentiation |

---

## Space Complexity Reference

| Structure | Space |
|-----------|-------|
| Array of n | O(n) |
| 2D array n×m | O(n×m) |
| Hash map | O(n) |
| Recursion stack depth h | O(h) |
| BFS queue | O(width of graph) |
| DFS stack | O(height of graph) |

---

## Most Common Patterns by Category

### Arrays
- Two Sum → Hash Map
- Max Subarray → Kadane's
- Trapping Rain Water → Two Pointers
- Merge Intervals → Sort + Linear Scan
- Product Except Self → Prefix/Suffix Pass

### Strings
- Anagram → Counter / Sort
- Longest Substring → Sliding Window
- Pattern Search → KMP / Rabin-Karp
- Palindrome → Expand Around Centre

### Trees
- Inorder/Preorder/Postorder → DFS
- Level Order → BFS
- Path Sum → DFS
- Lowest Common Ancestor → DFS Post-order

### Graphs
- Shortest Path (unweighted) → BFS
- Shortest Path (weighted) → Dijkstra
- Detect Cycle (undirected) → Union-Find
- Detect Cycle (directed) → DFS 3-colour
- Topological Sort → Kahn's or DFS

### Dynamic Programming
| Problem type | Base case | Transition |
|---|---|---|
| Fibonacci | dp[0]=0, dp[1]=1 | dp[i] = dp[i-1]+dp[i-2] |
| Climb stairs | dp[1]=1, dp[2]=2 | dp[i] = dp[i-1]+dp[i-2] |
| Coin change | dp[0]=0 | dp[i] = min(dp[i-coin]+1) |
| Knapsack | dp[0][w]=0 | dp[i][w] = max(skip, take) |
| LCS | dp[i][0]=dp[0][j]=0 | match: +1, else: max |
