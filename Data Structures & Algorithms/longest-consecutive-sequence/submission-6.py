class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     s = set(nums)   
     if len(nums)!=0:   
        final = []
        for i in s:
        
            l = 1

            if i-1 not in s:
                k = 1
                while i + k in s:    
                    l = l + 1
                    k = k + 1

            final.append(l)

        max = 0 
        for i in final:
            if i>max:
                max = i
        return max
     else:
        return 0

        
