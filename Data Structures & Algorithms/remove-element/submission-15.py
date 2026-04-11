class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
     left = 0 
     right = len(nums) - 1
    
    
     while left < right:

        while nums[right] == val:
            right = right - 1
            if right < 0:
                break
       

        if nums[left] == val:
            nums[left],nums[right] = nums[right], nums[left]
        
        left = left + 1
    
     k = 0 
     for i in nums:
        if i != val:
            k = k + 1
        else:
            break
     return k