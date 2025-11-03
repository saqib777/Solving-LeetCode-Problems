Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

**Solution**

Intuition
The left and right subtrees of every node differ in height by at most 1. Since the array is sorted, the middle element naturally becomes the root of the BST. (That’s because elements before it are smaller → left subtree, and elements after it are larger → right subtree.)

Approach
Find the middle element of the array — that becomes the root.

Recursively: The left half of the array builds the left subtree. The right half builds the right subtree.

Stop when the subarray is empty (base case).

Complexity
Time complexity: O(n)
Space complexity: O(log n
Code

```
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])   # LeetCode provides TreeNode
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

```
