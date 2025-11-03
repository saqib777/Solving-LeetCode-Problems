You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

**Solution**

Intuition
We’re given a number represented as an array of digits, e.g.
[1,2,3] → 123.

We need to add 1 to this number and return the new digits array.

The tricky part comes when digits carry over — for example:

[1,2,9] → should become [1,3,0] (since 129 + 1 = 130)

[9,9,9] → should become [1,0,0,0] (since 999 + 1 = 1000)

So, we must handle the carry correctly from the least significant digit (rightmost) toward the most significant (leftmost).

Approach
Start from the end of the list
The last digit (digits[-1]) is the ones place — the one we add +1 to.

Add 1 and handle carry
Add 1 to the current digit.

If the result is less than 10, we’re done — just return the array.

If the result is 10, set the current digit to 0 (carry over) and move to the previous digit.

If all digits roll over (like [9,9,9])
After processing all digits, if we still have a carry (e.g. all became 0),
we just insert 1 at the front → [1,0,0,0].

Complexity
Time complexity:
O(n) - we may visit each digit once

Space complexity:
O(1) — done in-place (except when we add one new digit in front)

Code
```
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Traverse the digits in reverse
        for i in range(n - 1, -1, -1):
            digits[i] += 1  # add 1 to the current digit
            
            if digits[i] < 10:
                return digits  # no carry, done
            else:
                digits[i] = 0  # carry to the next digit
        
        # If loop finishes, all digits were 9 (e.g., [9,9,9])
        return [1] + digits
```
