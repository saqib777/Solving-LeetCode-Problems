Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

Solutions

Intuition
the number that appears more than n / 2 times in the array.
You’re guaranteed that such an element always exists. A dictionary to count occurrences → O(n) time, O(n) space. But the question challenges us to do it in O(n) time and O(1) space**.

Approach
Start with count = 0.

As you iterate:

If count == 0, set the current number as the candidate.

If the number equals the candidate → increment count.

Else → decrement count.

At the end, the candidate is your majority element.

Complexity
Time complexity: O(n)
Space complexity: O(1)

Code
```
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```
