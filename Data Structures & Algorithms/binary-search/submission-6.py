class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_index = 0 
        upper_index = len(nums) - 1
        return self.binary_search(nums, target, lower_index, upper_index)

    def binary_search(self,nums, target, lower_index, upper_index):

        try:
            mid = lower_index +  (upper_index-lower_index)//2

            if nums[mid] == target:
                return mid
            
            elif target > nums[mid]:
                lower_index = mid + 1
                return self.binary_search(nums, target, lower_index, upper_index )
            
            elif target < nums[mid]:
                upper_index = mid - 1
                return self.binary_search(nums, target, lower_index, upper_index)
        except:
            return -1