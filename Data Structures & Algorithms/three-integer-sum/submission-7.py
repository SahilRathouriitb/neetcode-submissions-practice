class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        store = list()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] < target:
                    left = left + 1
                elif nums[left] + nums[right] > target:
                    right = right - 1

                elif (left > i+1) and (nums[left] == nums[left-1]):
                    left = left + 1
                else:
                    k = [nums[i], nums[left], nums[right]]
                    store.append(k)
                    left = left + 1

        return store

