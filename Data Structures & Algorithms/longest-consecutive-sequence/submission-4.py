class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     s = set(nums)   
     if len(nums)!=0:   
        final = []
        for i in s:
        
            l = 1

            if i-1 not in s:
                for k in range(len(s)):
                    if i + k + 1 in s:
                        l = l + 1
                    else:
                        break

            final.append(l)
    
        final.sort()
        return final[-1]
     else:
        return 0

        
