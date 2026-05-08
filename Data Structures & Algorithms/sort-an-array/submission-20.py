class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Let's try to solve this problem using Selection Sort

        for i in range(len(nums)-1):
            min = i

            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[i],nums[min] = nums[min],nums[i]
            # Here we will have the index of the smallest element in the array


        return nums