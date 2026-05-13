"""
LeetCode #206 — Reverse Linked List
Difficulty: Easy
Pattern: Iterative Pointer Reversal
Time: O(n) | Space: O(1) iterative | O(n) recursive

Problem:
    Given head of a singly linked list, reverse it and return new head.

Approach (iterative):
    Three pointers: prev, current, next_node.
    Walk through list reversing each pointer.
    When current is None, prev is the new head.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    """Iterative — O(1) space."""
    prev    = None
    current = head

    while current:
        next_node    = current.next
        current.next = prev
        prev         = current
        current      = next_node

    return prev


def reverse_list_recursive(head: ListNode, prev: ListNode = None) -> ListNode:
    """
    Recursive — O(n) stack space.
    Cleaner but risks stack overflow on very long lists.
    """
    if not head:
        return prev
    next_node    = head.next
    head.next    = prev
    return reverse_list_recursive(next_node, head)


# ── Helpers ────────────────────────────────────────────────────────────────────
def build(vals):
    if not vals: return None
    h = ListNode(vals[0]); c = h
    for v in vals[1:]: c.next = ListNode(v); c = c.next
    return h

def to_list(node):
    r = []
    while node: r.append(node.val); node = node.next
    return r


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic():
    assert to_list(reverse_list(build([1,2,3,4,5]))) == [5,4,3,2,1]

def test_two_elements():
    assert to_list(reverse_list(build([1,2]))) == [2,1]

def test_single():
    assert to_list(reverse_list(build([1]))) == [1]

def test_empty():
    assert reverse_list(None) is None

def test_recursive():
    assert to_list(reverse_list_recursive(build([1,2,3,4,5]))) == [5,4,3,2,1]

def test_both_agree():
    assert to_list(reverse_list(build([3,1,4,1,5]))) == \
           to_list(reverse_list_recursive(build([3,1,4,1,5])))

if __name__ == "__main__":
    print(to_list(reverse_list(build([1,2,3,4,5]))))   # [5,4,3,2,1]
