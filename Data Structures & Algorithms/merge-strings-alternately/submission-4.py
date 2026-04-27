class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        p1 = 0
        p2 = 0
        l = []

        while (p1 < len(word1)) and (p2 < len(word2)):

            l.append(word1[p1])
            p1 += 1
            l.append(word2[p2])
            p2 += 1

        if (p1 == len(word1)) and (p2 < len(word2)):
            while p2 < len(word2):
                l.append(word2[p2])
                p2 += 1
        elif (p2 == len(word2)) and (p1 < len(word1)):
            while p1 < len(word1):
                l.append(word1[p1])
                p1 += 1

        return "".join(l) 



