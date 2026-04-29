class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = 1

        while left < len(nums)-1:

            if (right - left <= k):

                if nums[left] == nums[right]:
                    return True
                elif right < len(nums)-1:
                    right += 1
                elif right == len(nums)-1:
                    left = left + 1
                    right = left + 1

            if right - left > k:
                left = left + 1
                right = left + 1
        
        return False

        