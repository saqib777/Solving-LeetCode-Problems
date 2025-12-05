```
448. Find All Numbers Disappeared in an Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

```

```
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        # Mark seen numbers by making nums[x-1] negative
        for x in nums:
            index = abs(x) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Values whose indices stay positive are the missing ones
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result
```
