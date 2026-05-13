"""
LeetCode #15 — 3Sum
Difficulty: Medium
Pattern: Sort + Two Pointers
Time: O(n²) | Space: O(1) ignoring output

Problem:
    Find all unique triplets in array that sum to zero.
    No duplicate triplets in output.

Approach:
    Sort the array.
    Fix one element at index i.
    Use two pointers for the remaining pair.
    Skip duplicates at every level to ensure uniqueness.
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue   # skip duplicate fixed element

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left]  == nums[left + 1]:  left  += 1
                while left < right and nums[right] == nums[right - 1]: right -= 1
                left  += 1
                right -= 1
            elif total < 0:
                left  += 1
            else:
                right -= 1

    return result


# ── Tests ──────────────────────────────────────────────────────────────────────
def sorted_result(r): return sorted([sorted(t) for t in r])

def test_basic():
    assert sorted_result(three_sum([-1,0,1,2,-1,-4])) == [[-1,-1,2],[-1,0,1]]

def test_all_zeros():
    assert three_sum([0,0,0]) == [[0,0,0]]

def test_no_result():
    assert three_sum([1,2,3]) == []

def test_empty():
    assert three_sum([]) == []

def test_two_elements():
    assert three_sum([0,1]) == []

def test_duplicates_handled():
    assert sorted_result(three_sum([-2,0,0,2,2])) == [[-2,0,2]]

def test_all_negative():
    assert three_sum([-4,-3,-2,-1]) == []

if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))   # [[-1,-1,2],[-1,0,1]]
    print(three_sum([0, 0, 0]))                 # [[0,0,0]]
