"""
LeetCode #104 — Maximum Depth of Binary Tree
Difficulty: Easy
Pattern: DFS Recursive
Time: O(n) | Space: O(h) — h = height of tree

Problem:
    Return the maximum depth of a binary tree.
    Depth = number of nodes along the longest path from root to leaf.

Approach:
    Recursively compute the height of left and right subtrees.
    Add 1 for the current node.
    Base case: None → 0
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """Recursive DFS."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_iterative(root: TreeNode) -> int:
    """
    BFS iterative — level by level, count levels.
    Time: O(n), Space: O(w) — w = max width.
    """
    from collections import deque
    if not root:
        return 0
    depth = 0
    queue = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
    return depth


# ── Helpers ────────────────────────────────────────────────────────────────────
def build(vals, i=0):
    if i >= len(vals) or vals[i] is None: return None
    n = TreeNode(vals[i])
    n.left  = build(vals, 2*i+1)
    n.right = build(vals, 2*i+2)
    return n


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic():          assert max_depth(build([3,9,20,None,None,15,7])) == 3
def test_single():         assert max_depth(build([1,None,2])) == 2
def test_empty():          assert max_depth(None) == 0
def test_single_node():    assert max_depth(TreeNode(1)) == 1
def test_left_skewed():    assert max_depth(build([1,2,None,3])) == 3
def test_both_agree():
    trees = [[3,9,20,None,None,15,7],[1,None,2],[1,2,None,3]]
    for vals in trees:
        assert max_depth(build(vals)) == max_depth_iterative(build(vals))

if __name__ == "__main__":
    print(max_depth(build([3,9,20,None,None,15,7])))   # 3
    print(max_depth(build([1,None,2])))                 # 2
