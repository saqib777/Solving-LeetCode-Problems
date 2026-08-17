"""
LeetCode #128 — Longest Consecutive Sequence
Difficulty: Medium
Pattern: Hash Set with Sequence Start Detection
Time: O(n) | Space: O(n)

Problem:
    Given an unsorted array of integers, return the length of the
    longest consecutive sequence (e.g. 1,2,3,4).

Constraint: must run in O(n) — no sorting allowed.

Approach:
    Add all numbers to a set for O(1) lookup.
    For each number, only start counting if it is the START of a
    sequence (i.e. num-1 is NOT in the set).
    Count upward from there.

Why O(n): each number is visited at most twice —
once to check if it is a start, once inside a counting loop.
"""


def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    best    = 0

    for num in num_set:
        if num - 1 not in num_set:   # sequence start
            current = num
            length  = 1

            while current + 1 in num_set:
                current += 1
                length  += 1

            best = max(best, length)

    return best


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic():
    assert longest_consecutive([100,4,200,1,3,2]) == 4

def test_longer():
    assert longest_consecutive([0,3,7,2,5,8,4,6,0,1]) == 9

def test_empty():
    assert longest_consecutive([]) == 0

def test_single():
    assert longest_consecutive([5]) == 1

def test_all_same():
    assert longest_consecutive([1,1,1,1]) == 1

def test_no_consecutive():
    assert longest_consecutive([1,3,5,7]) == 1

def test_negatives():
    assert longest_consecutive([-3,-2,-1,0,1]) == 5

def test_large_gap():
    assert longest_consecutive([1,2,3,100,101,102,103]) == 4

if __name__ == "__main__":
    print(longest_consecutive([100,4,200,1,3,2]))         # 4
    print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))    # 9
