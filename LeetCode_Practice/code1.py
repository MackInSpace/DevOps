#Problem 2235
"""class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2"""

#Problem 1929
"""class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums"""

#Problem 1512
"""class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count"""