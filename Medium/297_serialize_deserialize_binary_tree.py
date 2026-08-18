"""
LeetCode #297 — Serialize and Deserialize Binary Tree
Difficulty: Hard (listed as Medium in some versions)
Pattern: BFS Level-Order Serialization
Time: O(n) encode | O(n) decode
Space: O(n)

Problem:
    Design an algorithm to serialize a binary tree to a string
    and deserialize that string back to the original tree.

Approach:
    BFS serialization: level-order with 'N' for null nodes.
    Compact form: trim trailing nulls.
    Deserialization: rebuild level-by-level using a queue.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


def serialize(root: TreeNode) -> str:
    if not root:
        return "N"
    result = []
    queue  = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("N")
    while result and result[-1] == "N":
        result.pop()
    return ",".join(result)


def deserialize(data: str) -> TreeNode:
    if not data or data == "N":
        return None
    vals   = data.split(",")
    root   = TreeNode(int(vals[0]))
    queue  = deque([root])
    i      = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] != "N":
            node.left = TreeNode(int(vals[i]))
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] != "N":
            node.right = TreeNode(int(vals[i]))
            queue.append(node.right)
        i += 1
    return root


def to_list(root):
    if not root: return []
    r, q = [], deque([root])
    while q:
        n = q.popleft()
        r.append(n.val if n else None)
        if n: q.append(n.left); q.append(n.right)
    while r and r[-1] is None: r.pop()
    return r


# ── Tests ──────────────────────────────────────────────────────────────────────
def roundtrip(root): return deserialize(serialize(root))

def test_basic():
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert to_list(roundtrip(root)) == to_list(root)

def test_empty():
    assert serialize(None) == "N"
    assert deserialize("N") is None

def test_single():
    rt = roundtrip(TreeNode(42))
    assert rt.val == 42 and rt.left is None and rt.right is None

def test_left_skewed():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert to_list(roundtrip(root)) == [1,2,3]

def test_negative_values():
    root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
    rt   = roundtrip(root)
    assert rt.val == -1

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    print(serialize(root))
    print(to_list(deserialize(serialize(root))))
