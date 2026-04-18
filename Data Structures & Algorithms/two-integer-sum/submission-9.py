class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in mappa:
                return [mappa[t], i]
            mappa[n] = i