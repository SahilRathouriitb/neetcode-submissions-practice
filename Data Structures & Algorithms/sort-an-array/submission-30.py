import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums)-1)
        return nums

   

    def quick_sort(self,nums, left, right):
        if left >= right:
            return nums

        # random pivot
        pivot = nums[random.randint(left, right)]

        lt = left       # < pivot
        i = left        # current
        gt = right      # > pivot

        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1

        # recurse only on unequal parts
        self.quick_sort(nums, left, lt - 1)
        self.quick_sort(nums, gt + 1, right)
        return nums