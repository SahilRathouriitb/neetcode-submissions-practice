class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = height[0]
        right_max = height[len(height)-1]
        left = 1
        right = len(height) - 2
        water = 0

        while left <= right:

            if left_max <= right_max:
                ok = left_max - height[left]
                if ok > 0:
                    water = water + ok
                left_max = max(left_max, height[left])
                left += 1
            
            elif left_max > right_max:
                ok = right_max - height[right]
                if ok > 0:
                    water = water + ok
                right_max = max(right_max, height[right])
                right = right - 1
        
        return water





