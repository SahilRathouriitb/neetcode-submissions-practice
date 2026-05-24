class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = left + (right - left)//2
            # i need a for loop to check if mid is valid or not
            sum_ = 0
            sub_arrays = 0
            for i in nums:
                sum_ = sum_ + i
                if sum_ > mid:
                    sub_arrays += 1
                    sum_ = i 
            if sub_arrays + 1 <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left



        