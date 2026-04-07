class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums)-1

        while left<=right:

            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

        if target<nums[mid]:
          if mid > 0:  
            return mid
          else:
            return 0
        else:
            return mid+1
        