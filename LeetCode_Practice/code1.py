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
class Solution:
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

    print("All tests passed.")
