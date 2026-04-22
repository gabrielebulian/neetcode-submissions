class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        n = len(nums)
        res = [1]*n
        prefix = [1]*n
        suffix = [1]*n
        for i in range(1,len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) -1 , 0, -1):
            suffix[i - 1] = suffix[i] * nums[i]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res
        
