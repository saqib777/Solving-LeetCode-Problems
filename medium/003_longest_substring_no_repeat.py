"""
LeetCode #3 — Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Sliding Window + Hash Set
Time: O(n) | Space: O(min(n, m)) — m = charset size

Problem:
    Given a string, return the length of the longest substring
    without repeating characters.

Approach:
    Expand right pointer, shrink left pointer when a duplicate
    appears. Track characters in a set.
    Update max length after each valid window.
"""


def length_of_longest_substring(s: str) -> int:
    char_set   = set()
    left       = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic():      assert length_of_longest_substring("abcabcbb") == 3
def test_all_same():   assert length_of_longest_substring("bbbbb") == 1
def test_mixed():      assert length_of_longest_substring("pwwkew") == 3
def test_empty():      assert length_of_longest_substring("") == 0
def test_single():     assert length_of_longest_substring("a") == 1
def test_all_unique(): assert length_of_longest_substring("abcdef") == 6
def test_spaces():     assert length_of_longest_substring("ab c") == 4

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("pwwkew"))    # 3
