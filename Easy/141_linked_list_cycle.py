"""
LeetCode #141 — Linked List Cycle
Difficulty: Easy
Pattern: Fast and Slow Pointers (Floyd's Cycle Detection)
Time: O(n) | Space: O(1)

Problem:
    Return True if the linked list contains a cycle.

Approach:
    Two pointers — slow moves 1 step, fast moves 2 steps.
    If there is a cycle, fast will eventually lap slow and they meet.
    If no cycle, fast reaches None.

Why it works:
    In a cycle of length c, fast gains 1 step per iteration on slow.
    They will meet within at most c iterations after both enter the cycle.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


# ── Helpers ────────────────────────────────────────────────────────────────────
def build_with_cycle(vals: list, pos: int):
    """pos = -1 means no cycle."""
    if not vals: return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_cycle_exists():
    assert has_cycle(build_with_cycle([3,2,0,-4], 1)) == True

def test_no_cycle():
    assert has_cycle(build_with_cycle([1,2], -1)) == False

def test_single_self_loop():
    assert has_cycle(build_with_cycle([1], 0)) == True

def test_single_no_loop():
    assert has_cycle(build_with_cycle([1], -1)) == False

def test_empty():
    assert has_cycle(None) == False

def test_cycle_at_head():
    assert has_cycle(build_with_cycle([1,2,3,4,5], 0)) == True

def test_long_no_cycle():
    assert has_cycle(build_with_cycle(list(range(100)), -1)) == False

if __name__ == "__main__":
    print(has_cycle(build_with_cycle([3,2,0,-4], 1)))   # True
    print(has_cycle(build_with_cycle([1,2], -1)))        # False
