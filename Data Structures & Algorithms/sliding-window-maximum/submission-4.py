class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0 
        right = k-1 
        output = []
        
        m = -10001
        for i in range(left, left + k):
            m = max(m, nums[i])
        output.append(m)

        left += 1
        right += 1
        while right < len(nums):
            m = -10001
            for i in range(left, left + k):
                m = max(m, nums[i])
            output.append(m)
            left += 1
            right += 1
        return output
            

