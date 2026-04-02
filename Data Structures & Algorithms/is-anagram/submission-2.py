class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            a = []
            b = []
            for i in range(len(s)):
                a.append(s[i])
                b.append(t[i])
            a.sort()
            b.sort()
            if (a == b):
                return True
            else:
                return False

        else:
            return False