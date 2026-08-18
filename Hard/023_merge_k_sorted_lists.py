"""
LeetCode #23 — Merge k Sorted Lists
Difficulty: Hard
Pattern: Min-Heap (Priority Queue)
Time: O(n log k) — n total nodes, k lists, heap size k
Space: O(k) — heap stores at most k nodes

Problem:
    Merge k sorted linked lists into one sorted linked list.

Approach — Min-Heap:
    Push the head of every non-empty list into a min-heap.
    Pop the smallest node, add to result, push its next node.
    Repeat until heap is empty.

Alternative — Divide and Conquer:
    Merge pairs of lists recursively.
    Also O(n log k), cleaner code, no heap needed.
"""

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


def merge_k_lists_heap(lists: list) -> ListNode:
    """Min-heap approach."""
    heap  = []
    for node in lists:
        if node:
            heapq.heappush(heap, node)

    dummy   = ListNode(0)
    current = dummy

    while heap:
        node         = heapq.heappop(heap)
        current.next = node
        current      = current.next
        if node.next:
            heapq.heappush(heap, node.next)

    return dummy.next


def merge_k_lists_divide(lists: list) -> ListNode:
    """Divide and conquer approach — no heap needed."""
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    def merge_two(l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1; l1 = l1.next
            else:
                cur.next = l2; l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            merged.append(merge_two(l1, l2))
        lists = merged

    return lists[0]


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
def test_heap_basic():
    lists = [build([1,4,5]), build([1,3,4]), build([2,6])]
    assert to_list(merge_k_lists_heap(lists)) == [1,1,2,3,4,4,5,6]

def test_divide_basic():
    lists = [build([1,4,5]), build([1,3,4]), build([2,6])]
    assert to_list(merge_k_lists_divide(lists)) == [1,1,2,3,4,4,5,6]

def test_empty_input():
    assert merge_k_lists_heap([]) is None

def test_all_empty_lists():
    assert merge_k_lists_heap([None, None]) is None

def test_single_list():
    assert to_list(merge_k_lists_heap([build([1,2,3])])) == [1,2,3]

def test_both_agree():
    lists1 = [build([1,4,5]), build([1,3,4]), build([2,6])]
    lists2 = [build([1,4,5]), build([1,3,4]), build([2,6])]
    assert to_list(merge_k_lists_heap(lists1)) == \
           to_list(merge_k_lists_divide(lists2))

if __name__ == "__main__":
    lists = [build([1,4,5]), build([1,3,4]), build([2,6])]
    print(to_list(merge_k_lists_heap(lists)))   # [1,1,2,3,4,4,5,6]
