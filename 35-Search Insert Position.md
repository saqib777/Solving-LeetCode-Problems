Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

**Solution:**

Intuition
We have a sorted array and need to find the position of a target number. If it’s present, return its index. If it’s not present, return the index where it should be inserted to keep the array sorted.Because the array is sorted, a binary search is the best choice, giving us the required O(log n) time complexity.

Approach
Initialize two pointers:
left = 0
right = len(nums) - 1

While left <= right:
Find the middle: mid = (left + right) // 2
If nums[mid] == target, return mid
If nums[mid] < target, search in the right half → left = mid + 1
Else, search in the left half → right = mid - 1

If not found, left will end up at the insert position, so return left.

Complexity
Time complexity: O(log n)

Space complexity:
O(1)

Code

```
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
```
