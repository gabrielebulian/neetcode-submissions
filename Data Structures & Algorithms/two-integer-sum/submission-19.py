class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa = {}
        for i,x in enumerate(nums):
            t = target - x
            if t not in mappa:
                mappa[x] = i
            else: return [mappa[t], i]