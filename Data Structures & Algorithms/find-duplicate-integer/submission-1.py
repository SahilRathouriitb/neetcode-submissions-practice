class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        dict = {}
        for i in nums:
            if i in dict:
                return i 
            else:
                dict[i] = None