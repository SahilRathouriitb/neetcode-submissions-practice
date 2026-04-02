class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        j = len(s)-1
        for i in range(j):
            
            sum = sum + abs(ord(s[i+1])-ord(s[i]))

        return sum
