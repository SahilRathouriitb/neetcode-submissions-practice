class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0
        while i < len(nums):
            if i != 0 and nums[i] < nums[i-1]:
                break
            i += 1

        if i == len(nums):
            left = 0 
            right = len(nums) - 1
        
        else:
            i = i - 1
            if nums[0] <= target <= nums[i]:
                left = 0
                right = i
            else:
                left = i+1 
                right = len(nums) - 1
        
        while left <= right:

            mid = left + (right-left)//2

            if nums[mid] == target:
                return True

            elif target > nums[mid]:
                left = mid + 1
            
            elif target < nums[mid]:
                right = mid - 1
        return False