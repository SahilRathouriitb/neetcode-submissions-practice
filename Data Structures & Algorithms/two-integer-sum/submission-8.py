class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = (nums[i],i)
        
        nums.sort()
        left = 0 
        right = len(nums) - 1

        while left<right:
            if nums[left][0] + nums[right][0] > target:
                right = right - 1
            elif nums[left][0] + nums[right][0] < target:
                left = left + 1
            else:
                k = [nums[left][1], nums[right][1]]
                k.sort()
                return k