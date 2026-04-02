class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = len(nums) - 1
        for i in range(len(nums)):
           if i < len(nums)-1: 
            if nums[i+1] - nums[i] < 0:
                return nums[i+1]
           if i == (len(nums)-1) and nums[0] - nums[i] < 0:
                return nums[0]
