class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        pointer = 0

        while i < len(nums):

            if ((i > 0) and (nums[i] != nums[i-1])) or (i == 0):
                nums[pointer] = nums[i]
                pointer = pointer + 1
            
            i = i + 1
        
        return pointer 
              
