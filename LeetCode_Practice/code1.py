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

#Problem 1733
"""class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:"""
        # need an answer still

#Problem 58
"""class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])"""

#Problem 3
"""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1
            char_index[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("dvdf", 3),
        ("abba", 2),
    ]

    for s, expected in tests:
        got = sol.lengthOfLongestSubstring(s)
        print(f"input={s!r:10} expected={expected} got={got}")
        assert got == expected, (s, expected, got)

    print("All tests passed.")"""

#Problem 15
"""class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
            
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return res"""

#Problem 36
"""class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         rows = [set() for _ in range(9)]
         cols = [set() for _ in range(9)]
         boxes = [set() for _ in range(9)]

         for i in range(9):
             for j in range(9):
                 num = board[i][j]
                 if num != ".":
                     box_index = (i // 3) * 3 + j // 3
                     if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                         return False
                     rows[i].add(num)
                     cols[j].add(num)
                     boxes[box_index].add(num)
         return True"""

#Problem 27
"""class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k"""

#Problem 48
"""class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]"""

#Problem 121
"""class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit"""

#Problem 812
"""class Solution: 
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0.0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    area = 0.5 * abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0] * (points[i][1] - points[j][1]))
                    result = max(result, area)
        return result"""

#Problem 11
"""class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area"""

#Problem 41
"""class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1"""

#Problem 174
"""class Solution:
    def calculateMinimumHP(self, dungeon: List [List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = max(1, dp[m - 1][i + 1] - dungeon[m - 1][i])
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]"""

#Problem 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]