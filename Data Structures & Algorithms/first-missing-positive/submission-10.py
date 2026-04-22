class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
                nums[i] = [nums[i],False]

        for i in range(len(nums)):

                if 1<=nums[i][0]<=len(nums):
                        index = nums[i][0] - 1
                        nums[index][1] = True

        for i in range(len(nums)):

                if nums[i][1] == False:
                        return i+1
        
        return len(nums)+ 1