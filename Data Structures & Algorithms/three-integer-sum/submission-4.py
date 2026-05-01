class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        store = list()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] < target:
                    left = left + 1
                elif nums[left] + nums[right] > target:
                    right = right - 1
                else:
                    k = [nums[i], nums[left], nums[right]]
                    k.sort()
                    if k not in store:
                        store.append(k)
                    left = left + 1

        return store

