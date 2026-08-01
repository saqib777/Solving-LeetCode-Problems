"""
LeetCode #39 — Combination Sum
Difficulty: Medium
Pattern: Backtracking with Pruning
Time: O(2^target) worst case | Space: O(target) recursion depth

Problem:
    Given distinct integers and a target, find all combinations
    that sum to target. Each number may be used unlimited times.

Approach:
    Sort candidates for early termination.
    Backtrack: at each step, include the current candidate and
    recurse (same index, reuse allowed) or move to next candidate.
    Prune: if candidate > remaining, stop (array is sorted).
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []
    path   = []

    def backtrack(start: int, remaining: int):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return result


# ── Tests ──────────────────────────────────────────────────────────────────────
def sorted_result(r): return sorted([sorted(t) for t in r])

def test_basic():
    result = sorted_result(combination_sum([2,3,6,7], 7))
    assert result == [[2,2,3],[7]]

def test_two_results():
    result = sorted_result(combination_sum([2,3,5], 8))
    assert result == [[2,2,2,2],[2,3,3],[3,5]]

def test_no_result():
    assert combination_sum([2], 3) == []

def test_single_candidate():
    assert combination_sum([3], 9) == [[3,3,3]]

def test_target_equals_candidate():
    assert combination_sum([1,2,3], 1) == [[1]]

def test_empty_candidates():
    assert combination_sum([], 5) == []

if __name__ == "__main__":
    print(combination_sum([2,3,6,7], 7))   # [[2,2,3],[7]]
    print(combination_sum([2,3,5], 8))     # [[2,2,2,2],[2,3,3],[3,5]]
