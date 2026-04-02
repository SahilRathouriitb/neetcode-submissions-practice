class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hash1 = dict()
        for i in s1:
         if i in hash1:
            hash1[i] = hash1[i] + 1
         else:
            hash1[i] = 1

        
        
        left = 0
        right = 0

        hash2 = dict()

        while right < len(s2):

            if s2[right] not in hash2:
                hash2[s2[right]] = 1
            else:
                hash2[s2[right]] = hash2[s2[right]] + 1

            #print(hash2, left, right)
            
            

            if (right - left + 1) == len(s1):
                if hash1 == hash2:
                    return True
                else:
                    hash2[s2[left]] = hash2[s2[left]] - 1
                    if hash2[s2[left]] == 0:
                        hash2.pop(s2[left])
                    left = left + 1

            right = right + 1
        
        return False