class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums)
        nums.sort()
        streak = 0
        streak_new = 1
        for i in range(len(nums)):
            if streak_new > streak:
                streak = streak_new
            streak_new = 1
            prev = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == prev + 1:
                    streak_new += 1
                    prev = nums[j]
        return streak
