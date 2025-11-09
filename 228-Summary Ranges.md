You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.

**Solution**

Intuition

Each range [a, b] is represented as:
"a->b" if there’s a sequence
"a" if it’s just one number
Return all these ranges as strings.

**Approach**

Mark the start of a new range.
Keep going while numbers are consecutive (nums[i] == nums[i-1] + 1).
When you find a break (or reach the end):
Add the range to the result list.
Reset the start.

**Complexity**

Time complexity: O(n)
Space complexity: O(1)

**Code**

```
class Solution:
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res

        start = nums[0]

        for i in range(1, len(nums)):
            # If the sequence breaks
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]

        # Add the final range
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(nums[-1]))

        return res
```
