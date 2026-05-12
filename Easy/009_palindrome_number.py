"""
LeetCode #9 — Palindrome Number
Difficulty: Easy
Pattern: Math (Reverse Half the Number)
Time: O(log n) | Space: O(1)

Problem:
    Given an integer, return True if it reads the same forwards and backwards.
    Negative numbers are never palindromes.
    Follow-up: solve without converting to string.

Approach:
    Negative numbers → False immediately.
    Numbers ending in 0 (except 0 itself) → False.
    Reverse only the second half of the number.
    Compare reversed half with the first half.
    This avoids integer overflow on full reversal.
"""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # Even length: x == reversed_half
    # Odd length:  x == reversed_half // 10 (middle digit discarded)
    return x == reversed_half or x == reversed_half // 10


def is_palindrome_string(x: int) -> bool:
    """String conversion approach — simpler but uses O(n) space."""
    s = str(x)
    return s == s[::-1]


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic_true():        assert is_palindrome(121)   == True
def test_negative():          assert is_palindrome(-121)  == False
def test_trailing_zero():     assert is_palindrome(10)    == False
def test_zero():              assert is_palindrome(0)     == True
def test_single_digit():      assert is_palindrome(7)     == True
def test_even_palindrome():   assert is_palindrome(1221)  == True
def test_not_palindrome():    assert is_palindrome(123)   == False
def test_large():             assert is_palindrome(1000021000001) == False

def test_both_agree():
    cases = [121, -121, 10, 0, 7, 1221, 123, 9009]
    for n in cases:
        assert is_palindrome(n) == is_palindrome_string(n)

if __name__ == "__main__":
    print(is_palindrome(121))    # True
    print(is_palindrome(-121))   # False
    print(is_palindrome(10))     # False
    print(is_palindrome(0))      # True
