"""
LeetCode #100 — Same Tree
Difficulty: Easy
Pattern: DFS Recursive
Time: O(n) | Space: O(h)

Problem:
    Given roots of two binary trees, return True if they are
    structurally identical and all nodes have the same values.

Approach:
    Recursively check:
    1. Both None → True
    2. One None, one not → False
    3. Values differ → False
    4. Recurse on both left and right subtrees
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return (is_same_tree(p.left,  q.left) and
            is_same_tree(p.right, q.right))


def is_same_tree_iterative(p: TreeNode, q: TreeNode) -> bool:
    """Iterative BFS using a queue of node pairs."""
    from collections import deque
    queue = deque([(p, q)])

    while queue:
        n1, n2 = queue.popleft()
        if not n1 and not n2:
            continue
        if not n1 or not n2 or n1.val != n2.val:
            return False
        queue.append((n1.left,  n2.left))
        queue.append((n1.right, n2.right))

    return True


# ── Helpers ────────────────────────────────────────────────────────────────────
def build(vals, i=0):
    if i >= len(vals) or vals[i] is None: return None
    n = TreeNode(vals[i])
    n.left  = build(vals, 2*i+1)
    n.right = build(vals, 2*i+2)
    return n


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_identical():
    assert is_same_tree(build([1,2,3]), build([1,2,3])) == True

def test_different_structure():
    assert is_same_tree(build([1,2]), build([1,None,2])) == False

def test_different_values():
    assert is_same_tree(build([1,2,1]), build([1,1,2])) == False

def test_both_empty():
    assert is_same_tree(None, None) == True

def test_one_empty():
    assert is_same_tree(TreeNode(1), None) == False

def test_iterative_agrees():
    trees = [([1,2,3],[1,2,3]),([1,2],[1,None,2])]
    for v1, v2 in trees:
        assert is_same_tree(build(v1), build(v2)) == \
               is_same_tree_iterative(build(v1), build(v2))

if __name__ == "__main__":
    print(is_same_tree(build([1,2,3]), build([1,2,3])))      # True
    print(is_same_tree(build([1,2]),   build([1,None,2])))   # False
