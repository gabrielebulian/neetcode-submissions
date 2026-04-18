class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occorrenze = {}
        for i in s:
            occorrenze[i] = occorrenze.get(i,0) + 1
        for i in t:
            if i not in occorrenze:
                return False
            occorrenze[i] -= 1
            if occorrenze[i] < 0:
                return False
        return True
    

        