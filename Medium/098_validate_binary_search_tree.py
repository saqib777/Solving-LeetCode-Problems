
"""
LeetCode #98 — Validate Binary Search Tree
Difficulty: Medium
Pattern: DFS with Min/Max Range Bounds
Time: O(n) | Space: O(h)

Problem:
    Return True if a binary tree is a valid BST.
    BST rule: left subtree < node < right subtree at EVERY level.

Common mistake:
    Checking only that left < root and root < right is WRONG.
    A node in the left subtree must be less than ALL ancestors, not just
    its direct parent. The range approach handles this correctly.

Approach:
    Pass down valid range [min_val, max_val] for each node.
    Initially (-inf, +inf). Narrow the range at each step.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    def validate(node, min_val, max_val) -> bool:
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (validate(node.left,  min_val,    node.val) and
                validate(node.right, node.val,   max_val))

    return validate(root, float('-inf'), float('inf'))


# ── Helpers ────────────────────────────────────────────────────────────────────
def build(vals, i=0):
    if i >= len(vals) or vals[i] is None: return None
    n = TreeNode(vals[i])
    n.left  = build(vals, 2*i+1)
    n.right = build(vals, 2*i+2)
    return n


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_valid_bst():
    assert is_valid_bst(build([2,1,3])) == True

def test_invalid_bst():
    assert is_valid_bst(build([5,1,4,None,None,3,6])) == False

def test_single_node():
    assert is_valid_bst(TreeNode(1)) == True

def test_empty():
    assert is_valid_bst(None) == True

def test_left_subtree_violation():
    root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(15)), TreeNode(20))
    assert is_valid_bst(root) == False

def test_duplicate_values():
    root = TreeNode(2, TreeNode(2), TreeNode(3))
    assert is_valid_bst(root) == False

def test_valid_three_levels():
    root = build([8,3,10,1,6,None,14,None,None,4,7])
    assert is_valid_bst(root) == True

if __name__ == "__main__":
    print(is_valid_bst(build([2,1,3])))             # True
    print(is_valid_bst(build([5,1,4,None,None,3,6])))  # False
