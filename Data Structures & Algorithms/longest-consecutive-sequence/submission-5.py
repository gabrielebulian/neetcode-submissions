class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0        
        nums.sort()
        streak = 1
        streak_new = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                streak_new += 1
            else: 
                streak = max(streak, streak_new)
                streak_new = 1
        return max(streak, streak_new)