# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# ans = [1,2,1,1,2,1]

#Approach 1 (Using Loop):
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        conc = []
        arrleng = len(nums)
        for i in range(2):
            for n in range(arrleng):
                conc.append(nums[n])
        return conc


# Approach 2 (Use Extend Method Python):
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums

# Approach 3 (Use of * Operator):
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums*2  

# Approach 4 (Use of + Operator):
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
