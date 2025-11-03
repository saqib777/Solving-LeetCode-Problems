**Intuition**

Start assuming the first string is the common prefix. For every other string, check if it starts with the prefix: If not, chop off the last character and check again. Keep going until all strings share the same prefix (or it becomes empty).

**Approach**
Horizontal Scanning

**Complexity**
Time complexity: O(S)

**Space complexity:
**O(1)

**Code**
```
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
```
        
