class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s2 = []
            t2 = []
            for char in s:
                s2.append(char)
            for char in t:
                t2.append(char)
            s2.sort()
            t2.sort()
            if s2 == t2:
                return True
        return False

        