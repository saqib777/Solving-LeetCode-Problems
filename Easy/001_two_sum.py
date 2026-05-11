"""
LeetCode #1 — Two Sum
Difficulty: Easy
Pattern: Hash Map (One-pass)
Time: O(n) | Space: O(n)

Problem:
    Given an array of integers and a target, return indices
    of the two numbers that add up to the target.
    Each input has exactly one solution. Same element not used twice.

Approach:
    For each number, check if its complement (target - num)
    is already in our hash map. If yes, return both indices.
    If no, store the current number and its index.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ── Tests ──────────────────────────────────────────────────────────────────────
import pytest

def test_basic():         assert two_sum([2,7,11,15], 9)  == [0,1]
def test_middle():        assert two_sum([3,2,4], 6)       == [1,2]
def test_duplicates():    assert two_sum([3,3], 6)          == [0,1]
def test_negatives():     assert two_sum([-1,-2,-3,-4], -7) == [2,3]
def test_no_solution():   assert two_sum([1,2,3], 100)      == []

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]
