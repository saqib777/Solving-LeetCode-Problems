
"""
LeetCode #238 — Product of Array Except Self
Difficulty: Medium
Pattern: Prefix and Suffix Product Pass
Time: O(n) | Space: O(1) — output array not counted

Problem:
    Return array where output[i] = product of all nums except nums[i].
    Must run in O(n) without using division.

Approach:
    Two-pass: compute prefix products left-to-right storing in result.
    Then multiply suffix products right-to-left in a single variable.

    result[i] = (product of all elements left of i)
                * (product of all elements right of i)
"""


def product_except_self(nums: list[int]) -> list[int]:
    n      = len(nums)
    result = [1] * n

    # Left pass: result[i] = product of nums[0..i-1]
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix   *= nums[i]

    # Right pass: multiply result[i] by product of nums[i+1..n-1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix    *= nums[i]

    return result


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic():
    assert product_except_self([1,2,3,4]) == [24,12,8,6]

def test_with_zero():
    assert product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]

def test_two_zeros():
    assert product_except_self([0,0,1]) == [0,0,0]

def test_two_elements():
    assert product_except_self([3,4]) == [4,3]

def test_negatives():
    assert product_except_self([-1,-2,-3]) == [6,3,2]

def test_single_element():
    assert product_except_self([5]) == [1]

def test_all_ones():
    assert product_except_self([1,1,1,1]) == [1,1,1,1]

if __name__ == "__main__":
    print(product_except_self([1,2,3,4]))     # [24,12,8,6]
    print(product_except_self([-1,1,0,-3,3])) # [0,0,9,0,0]
