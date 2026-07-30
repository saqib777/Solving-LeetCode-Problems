"""
LeetCode #226 — Invert Binary Tree
Difficulty: Easy
Pattern: DFS Recursive (Post-order)
Time: O(n) | Space: O(h)

Problem:
    Mirror a binary tree — swap every left and right child node.

Approach:
    Post-order DFS: recurse to leaves first, then swap children.
    One-liner in Python: swap left/right while recursing.

Famous note: this problem was tweeted by a Google engineer as one
he failed at a whiteboard interview. It's simple but a good test
of recursive thinking.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    """Recursive — clean and minimal."""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def invert_tree_iterative(root: TreeNode) -> TreeNode:
    """
    Iterative BFS — swap children level by level.
    Time: O(n), Space: O(w)
    """
    from collections import deque
    if not root:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    return root


# ── Helpers ────────────────────────────────────────────────────────────────────
def to_list(root):
    if not root: return []
    from collections import deque
    r, q = [], deque([root])
    while q:
        n = q.popleft()
        r.append(n.val if n else None)
        if n: q.append(n.left); q.append(n.right)
    while r and r[-1] is None: r.pop()
    return r

def build(vals, i=0):
    if i >= len(vals) or vals[i] is None: return None
    n = TreeNode(vals[i])
    n.left  = build(vals, 2*i+1)
    n.right = build(vals, 2*i+2)
    return n


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic():
    assert to_list(invert_tree(build([4,2,7,1,3,6,9]))) == [4,7,2,9,6,3,1]

def test_empty():
    assert invert_tree(None) is None

def test_single():
    assert to_list(invert_tree(TreeNode(1))) == [1]

def test_two_levels():
    assert to_list(invert_tree(build([1,2,3]))) == [1,3,2]

def test_iterative_agrees():
    vals = [4,2,7,1,3,6,9]
    assert to_list(invert_tree(build(vals))) == \
           to_list(invert_tree_iterative(build(vals)))

if __name__ == "__main__":
    print(to_list(invert_tree(build([4,2,7,1,3,6,9]))))   # [4,7,2,9,6,3,1]
