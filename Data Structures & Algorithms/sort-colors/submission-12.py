from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
       if len(nums) == 1:
            return 
       p0 = 0
       p2 = len(nums) - 1

       tracker = p0

       while tracker <= p2:
           
        while nums[p0] == 0:
               p0 += 1
               if p0 == len(nums):
                    return
    
        
        if tracker < p0:
            tracker = p0    

        while nums[p2] == 2:
               p2 -= 1
               if p2 < 0:
                    return

        if nums[tracker] == 0:
            nums[p0], nums[tracker] = nums[tracker], nums[p0]
        
        elif nums[tracker] == 2:
            nums[p2], nums[tracker] = nums[tracker], nums[p2]
        
        elif nums[tracker] == 1:
                tracker += 1
            
       print(nums)

        

            
