class Solution:
    def __init__(self):
        self.store = []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        for i in range(len(nums)):

            if i>0 and nums[i] == nums[i-1]:
                continue
            check = target - nums[i]
            self.threeSum(nums,check,nums[i],i)

        return self.store    
    

    def threeSum(self, nums: List[int], check, first_ele,index) -> List[List[int]]:
        for i in range(index+1,len(nums)):
            if i>(index+1) and (nums[i] == nums[i-1]):
                continue
            left = i + 1
            right = len(nums) - 1
            target = check - nums[i]
            while left < right:
                if nums[left] + nums[right] < target:
                    left = left + 1
                elif nums[left] + nums[right] > target:
                    right = right - 1

                elif (left > i+1) and (nums[left] == nums[left-1]):
                    left = left + 1
                else:
                    k = [first_ele, nums[i], nums[left], nums[right]]
                    self.store.append(k)
                    left = left + 1
        