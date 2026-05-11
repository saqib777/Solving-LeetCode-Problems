"""
LeetCode #20 — Valid Parentheses
Difficulty: Easy
Pattern: Stack
Time: O(n) | Space: O(n)

Problem:
    Given a string of brackets (), [], {}, return True if valid.
    Open brackets must be closed in the correct order.

Approach:
    Push opening brackets onto a stack.
    When we see a closing bracket, check if it matches the stack top.
    At the end, stack must be empty.
"""


def is_valid(s: str) -> bool:
    stack    = []
    matching = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_simple():       assert is_valid("()") == True
def test_mixed():        assert is_valid("()[]{}") == True
def test_wrong_order():  assert is_valid("(]") == False
def test_interleaved():  assert is_valid("([)]") == False
def test_nested():       assert is_valid("{[]}") == True
def test_empty():        assert is_valid("") == True
def test_unclosed():     assert is_valid("[") == False
def test_extra_close():  assert is_valid(")") == False

if __name__ == "__main__":
    print(is_valid("()[]{}"))   # True
    print(is_valid("([)]"))     # False
