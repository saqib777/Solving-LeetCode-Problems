# Problem Solving Checklist

Use this before writing a single line of code.
Rushing to code is the fastest way to waste time.

---

## Step 1 — Understand the Problem (2 min)

- [ ] Read the problem twice
- [ ] What is the input? What is the output?
- [ ] What does a valid answer look like?
- [ ] Are there constraints I need to note? (array size, value range)

---

## Step 2 — Work Through Examples (3 min)

- [ ] Trace through the given examples by hand
- [ ] Create your own simple example
- [ ] Create an edge case example
- [ ] What happens with empty input?
- [ ] What happens with a single element?
- [ ] What happens with all same values?

---

## Step 3 — Identify the Pattern (2 min)

Ask yourself:

| If the problem involves... | Think about... |
|---------------------------|----------------|
| Sorted array, find pair | Two Pointers |
| Subarray sum or length | Sliding Window |
| Count or find complement | Hash Map |
| Sorted array, O(log n) | Binary Search |
| Tree traversal | DFS or BFS |
| Shortest path | BFS or Dijkstra |
| Max/min with choices | DP or Greedy |
| All subsets | Backtracking or Bitmask |
| Linked list cycle | Fast and Slow Pointers |

---

## Step 4 — Plan Before Coding (3 min)

- [ ] State your approach in plain English first
- [ ] What data structures do you need?
- [ ] What is the time complexity of your plan?
- [ ] What is the space complexity?
- [ ] Is there a brute force? What is the optimal?

---

## Step 5 — Code (10-15 min)

- [ ] Write clean, readable code
- [ ] Use meaningful variable names
- [ ] Handle edge cases explicitly
- [ ] Do not optimise prematurely

---

## Step 6 — Test Your Code (5 min)

- [ ] Trace through your examples manually
- [ ] Test with empty input
- [ ] Test with single element
- [ ] Test with duplicates
- [ ] Test with negatives if applicable
- [ ] Does it handle the maximum constraint?

---

## Step 7 — Optimise (if time permits)

- [ ] Can you reduce time complexity?
- [ ] Can you reduce space complexity?
- [ ] Is there a cleaner way to write this?

---

## Complexity Reference

| Algorithm | Time | Space |
|-----------|------|-------|
| Brute force nested loops | O(n²) | O(1) |
| Hash map single pass | O(n) | O(n) |
| Two pointers on sorted | O(n) | O(1) |
| Binary search | O(log n) | O(1) |
| BFS / DFS on graph | O(V+E) | O(V) |
| Merge sort | O(n log n) | O(n) |
| DP tabulation | O(n*m) | O(n) |

---

## Interview Tips

- Always talk through your thinking — silence is worse than wrong
- Say "let me think about edge cases" before coding
- If stuck, start with brute force and improve
- Time yourself — easy: 15 min, medium: 25 min, hard: 35 min
