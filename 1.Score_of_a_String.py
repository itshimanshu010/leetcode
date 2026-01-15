# Example 1:

# Input: s = "code"
# Output: 24
# Explanation: The ASCII values of the characters in the given string are: 
# 'c' = 99, 'o' = 111, 'd' = 100, and 'e' = 101. 
# The score of s will be: |111 - 99| + |100 - 111| + |101 - 100|.

#Code:
class Solution:
    def scoreOfString(self, s: str) -> int:

# Approach:
class Solution:
    def scoreOfString(self, s:str) -> int:
        res = 0;
        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i+1]))
        return res
