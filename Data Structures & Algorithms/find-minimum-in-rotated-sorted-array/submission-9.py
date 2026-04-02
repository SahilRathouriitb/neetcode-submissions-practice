class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0 
        right = len(nums)-1

        while left<=right:

            if left == right:
                return nums[left]

            mid = left + (right-left)//2

            if nums[mid] > nums[right]:
                # this means the change point is on the right side
                left = mid + 1

            else:
                right = mid