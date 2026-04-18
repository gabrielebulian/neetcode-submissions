class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = sorted(s)
        ts = sorted(t)
        if ss == ts:
            return True
        return False
        