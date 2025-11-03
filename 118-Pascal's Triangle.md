Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

**Solution**

Intuition
Pascal’s Triangle looks like this (for 5 rows):
Every row starts and ends with 1, and each inner number = sum of the two numbers above it.

Approach
Start with the first row [1].

For each new row: Begin and end with 1. Each middle element = sum of two numbers above it.

Repeat until you’ve built numRows rows.

Complexity
Time complexity: O(n²)
Space complexity: O(n²)

Code

```
class Solution:
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)

            # Fill the middle values using previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

```
            
            triangle.append(row)

        return triangle
