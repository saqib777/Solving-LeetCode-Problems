**Intuition**
For every number in the list, check every other number that comes after it. If any two numbers add up to the target, return their indices.

##Approach
This is my first time appraoch to solve a problem online, so I used the brute force.

###Complexity
###Time complexity:O(n²)

##Space complexity: O(1) (constant space)

##Code
```class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []
```
