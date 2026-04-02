class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     s = set(nums)   
     if len(nums)!=0:   
        
        l = 1
        for i in s:
            m = 1
            if i-1 not in s:
                k = 1
                while i + k in s:    
                    m = m + 1
                    k = k + 1
                if m>l:
                    l = m
        return l
     else:
        return 0