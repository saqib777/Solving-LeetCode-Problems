"""
LeetCode #121 — Best Time to Buy and Sell Stock
Difficulty: Easy
Pattern: Greedy (Single Pass)
Time: O(n) | Space: O(1)

Problem:
    prices[i] = price of stock on day i.
    Buy on one day, sell on a later day.
    Return maximum profit. Return 0 if no profit possible.

Approach:
    Track the minimum price seen so far.
    At each day, compute profit if we sold today.
    Update maximum profit.
    We never need to look back — one pass is enough.
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    min_price      = float('inf')
    max_profit_val = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price

    return max_profit_val


# ── Tests ──────────────────────────────────────────────────────────────────────
def test_basic():         assert max_profit([7,1,5,3,6,4])   == 5
def test_no_profit():     assert max_profit([7,6,4,3,1])     == 0
def test_two_days():      assert max_profit([1,2])            == 1
def test_two_desc():      assert max_profit([2,1])            == 0
def test_empty():         assert max_profit([])               == 0
def test_single():        assert max_profit([5])              == 0
def test_all_same():      assert max_profit([3,3,3,3])        == 0
def test_buy_first():     assert max_profit([1,2,3,4,5])      == 4
def test_large_profit():  assert max_profit([1,100])          == 99

if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
    print(max_profit([7, 6, 4, 3, 1]))       # 0
