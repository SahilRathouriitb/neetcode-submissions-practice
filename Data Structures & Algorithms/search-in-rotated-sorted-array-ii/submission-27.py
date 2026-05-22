class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0 
        right = len(nums) - 1

        while left <= right:

          mid = left + (right - left)//2

          if nums[mid] == target:
               return True

          elif (nums[mid] == nums[right]) and (nums[mid] == nums[left]):
               # in such cases always go for the right side
               for i in range(mid + 1, right + 1):
                    if nums[i] == target:
                         return True
               right = mid - 1

          elif (nums[mid] <= nums[right]) and (nums[mid] < nums[left]):
               if nums[mid] < target <= nums[right]:
                    left = mid + 1
               else:
                    right = mid - 1
          
          elif (nums[mid] >= nums[left]):
               if nums[left] <= target < nums[mid]:
                    right = mid - 1
               else:
                    left = mid + 1
        return False