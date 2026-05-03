class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        pointer = 0

        while i < len(nums):

            if ((i > 0) and (nums[i] != nums[i-1])) or (i == 0):
                # This means this is a unique value
                nums[pointer] = nums[i]
                pointer = pointer + 1
            
            i = i + 1
        
        print(nums)
        print(pointer)
        return pointer 
              
