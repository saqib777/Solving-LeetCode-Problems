
"""
LeetCode #21 — Merge Two Sorted Lists
Difficulty: Easy
Pattern: Two Pointer (Iterative with Dummy Head)
Time: O(n + m) | Space: O(1)

Problem:
    Merge two sorted linked lists and return head of merged list.
    The merged list should be sorted.

Approach:
    Use a dummy head to simplify edge cases.
    Compare values at both list heads.
    Attach the smaller one to result, advance that pointer.
    Attach remaining list at the end.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy   = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next


def merge_two_lists_recursive(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Recursive variant — elegant but uses O(n+m) stack space.
    """
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val <= l2.val:
        l1.next = merge_two_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_recursive(l1, l2.next)
        return l2


# ── Helpers ────────────────────────────────────────────────────────────────────
def build(vals: list) -> ListNode:
    if not vals:
        return None
    head = ListNode(vals[0])
    cur  = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def to_list(node: ListNode) -> list:
    r = []
    while node:
        r.append(node.val)
        node = node.next
    return r


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic():
    assert to_list(merge_two_lists(build([1,2,4]), build([1,3,4]))) == [1,1,2,3,4,4]

def test_one_empty():
    assert to_list(merge_two_lists(None, build([1,2,3]))) == [1,2,3]

def test_both_empty():
    assert merge_two_lists(None, None) is None

def test_single_elements():
    assert to_list(merge_two_lists(build([1]), build([2]))) == [1,2]

def test_recursive_basic():
    assert to_list(merge_two_lists_recursive(build([1,2,4]), build([1,3,4]))) == [1,1,2,3,4,4]

if __name__ == "__main__":
    l1 = build([1, 2, 4])
    l2 = build([1, 3, 4])
    print(to_list(merge_two_lists(l1, l2)))   # [1,1,2,3,4,4]
