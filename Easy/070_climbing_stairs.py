"""
LeetCode #70 — Climbing Stairs
Difficulty: Easy
Pattern: Dynamic Programming (Fibonacci)
Time: O(n) | Space: O(1)

Problem:
    You climb n stairs. Each time you can take 1 or 2 steps.
    How many distinct ways can you reach the top?

Approach:
    climb(n) = climb(n-1) + climb(n-2)
    This is exactly the Fibonacci sequence offset by one.
    Space-optimised: only track previous two values.

    n=1: [1]               → 1 way
    n=2: [1+1, 2]          → 2 ways
    n=3: [1+1+1, 1+2, 2+1] → 3 ways
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


def climb_stairs_memo(n: int, memo: dict = {}) -> int:
    """Top-down memoization approach."""
    if n <= 2:
        return n
    if n not in memo:
        memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_one():          assert climb_stairs(1)  == 1
def test_two():          assert climb_stairs(2)  == 2
def test_three():        assert climb_stairs(3)  == 3
def test_five():         assert climb_stairs(5)  == 8
def test_ten():          assert climb_stairs(10) == 89
def test_large():        assert climb_stairs(45) == 1836311903

def test_both_agree():
    for n in range(1, 20):
        assert climb_stairs(n) == climb_stairs_memo(n, {})

if __name__ == "__main__":
    for i in range(1, 8):
        print(f"climb_stairs({i}) = {climb_stairs(i)}")
    # 1, 2, 3, 5, 8, 13, 21
