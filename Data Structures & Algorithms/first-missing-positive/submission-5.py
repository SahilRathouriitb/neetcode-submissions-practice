class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
                if nums[i] < 0:
                        nums[i] = 0 

        
        for i in range(len(nums)):  
                      
                        index = abs(nums[i]) - 1
                        if 0<= index < len(nums):
                           if nums[index] != 0: 
                                nums[index] = -abs(nums[index])
                           else:
                               nums[index] = -abs(nums[index] + len(nums)+ 10)    


        for i in range(1,len(nums)+1):
                
                if nums[i-1] >= 0:
                        return i
                
        return len(nums)+1