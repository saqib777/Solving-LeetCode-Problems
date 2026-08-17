
"""
LeetCode #49 — Group Anagrams
Difficulty: Medium
Pattern: Hash Map with Sorted String Key
Time: O(n * k log k) — n strings, k = max string length
Space: O(n * k)

Problem:
    Given a list of strings, group anagrams together.
    Return a list of grouped lists in any order.

Approach:
    Anagrams have identical sorted characters.
    Sort each string → use as key in hash map.
    Strings with same key belong to same group.

Optimised alternative:
    Count character frequencies (26 letters) as tuple key.
    Avoids sorting: O(n * k) time instead of O(n * k log k).
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Sort-based grouping."""
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def group_anagrams_count(strs: list[str]) -> list[list[str]]:
    """
    Count-based grouping — O(n * k) time, avoids sorting.
    Key = tuple of 26 character frequencies.
    """
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())


# ── Tests ──────────────────────────────────────────────────────────────────────
def sorted_groups(result):
    return sorted([sorted(g) for g in result])

def test_basic():
    result = sorted_groups(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    assert result == [["ate","eat","tea"],["bat"],["nat","tan"]]

def test_empty_string():
    result = sorted_groups(group_anagrams(["",""]))
    assert result == [["",""]]

def test_single_word():
    assert sorted_groups(group_anagrams(["abc"])) == [["abc"]]

def test_no_anagrams():
    result = sorted_groups(group_anagrams(["abc","def","ghi"]))
    assert result == [["abc"],["def"],["ghi"]]

def test_count_method_agrees():
    strs = ["eat","tea","tan","ate","nat","bat"]
    assert sorted_groups(group_anagrams(strs)) == \
           sorted_groups(group_anagrams_count(strs))

def test_empty_input():
    assert group_anagrams([]) == []

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
