219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 
**Constraints**:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

**Solution**

**Intuition**
an integer array nums
an integer k
Return True if there exist two equal elements such that their indices i and j satisfy

**Approach**
Keep track of the last seen index of each number.
For each new element:
If it has been seen before, check if the distance ≤ k.
If yes → return True.
Otherwise, update its latest index.

**Complexity:**

Time complexity: O(n)
Space complexity: O(n)

**Code**
```
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i

        return False\
```
