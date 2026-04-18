class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa = {}
        for i,x in enumerate(nums):
            t = target - x
            if t in mappa:
                return [mappa[t], i]
            mappa[x] = i