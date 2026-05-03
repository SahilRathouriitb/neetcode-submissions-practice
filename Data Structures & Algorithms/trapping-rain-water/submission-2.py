class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        water = 0
        left_high = height[0]

        
        stack= [height[len(height)-1]]
        for i in range(len(height)-2,0,-1):    
            if height[i] >= stack[-1]:
                stack.append(height[i])
        

        while i < len(height):

            if (i != 0) and i != (len(height)-1):
                if height[i] == stack[-1]:
                    stack.pop()
                right_high = stack[-1]
                ok = min(left_high, right_high) - height[i]
                if ok > 0:
                    water = water + ok
            
            left_high = max(left_high, height[i])
            i = i + 1
        return water
                

