class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
     left = 0 
     right = len(nums) - 1
     counter = 0
    
     while left < right:

        while nums[right] == val:
            counter = counter + 1
            right = right - 1
            if right < 0:
                break
       
        if nums[left] == val:
            nums[left],nums[right] = nums[right], nums[left]
        
        left = left + 1

     if right>=0:
      if (nums[right] == val):
        counter += 1  

     return len(nums)-counter