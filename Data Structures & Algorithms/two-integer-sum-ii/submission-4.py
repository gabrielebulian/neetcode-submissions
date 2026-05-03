class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            n = numbers[i]
            t = target - n
            if t not in seen:
                seen[n] = i + 1
            else: 
                j = seen.get(t,0)
                return [j, i + 1]
        
        




        