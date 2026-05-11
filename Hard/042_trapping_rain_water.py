"""
LeetCode #42 — Trapping Rain Water
Difficulty: Hard
Pattern: Two Pointers
Time: O(n) | Space: O(1)

Problem:
    Given elevation heights, compute total water trapped after rain.

Approach:
    Two pointers from each end. Maintain left_max and right_max.
    Process whichever side has the smaller max — that side's
    trapped water is min(left_max, right_max) - height[i].
    The other side guarantees at least right_max of support.

Why two pointers works:
    Water at i = min(max_left_of_i, max_right_of_i) - height[i]
    When left_max <= right_max, we know right side can support
    at least left_max height, so water = left_max - height[left].
"""


def trap(height: list[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max    = height[left]
    right_max   = height[right]
    water       = 0

    while left < right:
        if left_max <= right_max:
            left     += 1
            left_max  = max(left_max, height[left])
            water    += left_max - height[left]
        else:
            right    -= 1
            right_max = max(right_max, height[right])
            water    += right_max - height[right]

    return water


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_example1(): assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
def test_example2(): assert trap([4,2,0,3,2,5]) == 9
def test_empty():    assert trap([]) == 0
def test_flat():     assert trap([3,3,3]) == 0
def test_valley():   assert trap([5,0,5]) == 5
def test_single():   assert trap([5]) == 0

if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(trap([4,2,0,3,2,5]))               # 9
