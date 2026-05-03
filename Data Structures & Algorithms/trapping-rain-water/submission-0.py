class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        water = 0
        left_high = height[0]

        while i < len(height):

            if (i != 0) and i != (len(height)-1):
                right_high = self.right_highest(height, i)
                ok = min(left_high, right_high) - height[i]
                if ok > 0:
                    water = water + ok
            
            left_high = max(left_high, height[i])
            i = i + 1
        return water
                

                
    def right_highest(self,height, curr_index):
        k = 0
        for i in range(curr_index+1, len(height)):
            k = max(height[i],k)
        return k

