"""
LeetCode #53 — Maximum Subarray
Difficulty: Medium
Pattern: Kadane's Algorithm (Dynamic Programming)
Time: O(n) | Space: O(1)

Problem:
    Find the contiguous subarray with the largest sum.
    Return the sum.

Approach:
    Kadane's: at each index, decide whether to extend the
    current subarray or start fresh.
    current = max(num, current + num)
    Track global maximum throughout.
"""


def max_subarray(nums: list[int]) -> int:
    max_sum     = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum     = max(max_sum, current_sum)

    return max_sum


def max_subarray_with_indices(nums: list[int]) -> tuple[int, int, int]:
    """
    Variant: also return (start, end) indices of the subarray.
    Returns (max_sum, start_index, end_index).
    """
    max_sum     = nums[0]
    current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start  = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start   = temp_start
            end     = i

    return max_sum, start, end


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_mixed():       assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
def test_all_positive(): assert max_subarray([5,4,-1,7,8]) == 23
def test_single():      assert max_subarray([1]) == 1
def test_all_negative(): assert max_subarray([-3,-2,-1,-4]) == -1
def test_with_indices():
    s, start, end = max_subarray_with_indices([−2,1,-3,4,-1,2,1,-5,4])
    assert s == 6
    assert end >= start

if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(max_subarray([5,4,-1,7,8]))              # 23
