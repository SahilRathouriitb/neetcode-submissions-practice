class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     if len(nums)!=0:   
        final = []
        for i in set(nums):

            l = 1

            for k in range(len(set(nums))):
                if i + k + 1 in set(nums):
                    l = l + 1
                else:
                    break

            final.append(l)
    
        final.sort()
        return final[-1]
     else:
        return 0

        
