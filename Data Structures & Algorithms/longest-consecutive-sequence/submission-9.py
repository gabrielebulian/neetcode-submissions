class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        numset = set(nums)
        longest = 0
        for x in numset:
            if x - 1 not in numset:
                current = x
                streak = 1
                while current + 1 in numset:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        return longest