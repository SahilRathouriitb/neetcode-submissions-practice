class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[heights[0], 0]]
        i = 1
        max_area = heights[0] 

        while i < len(heights):

            if heights[i] >= stack[-1][0]:
                stack.append([heights[i], i])
                i += 1
            
            else:
                k = None
                p_count = 0
                while (heights[i]) < stack[-1][0]:
                    k = stack.pop()
                    max_area = max(max_area, k[0]*((i)-k[1]))
                    if len(stack) == 0:
                        break
                stack.append([heights[i],  k[1]])
                i += 1
    
        while len(stack) > 0:
            k = stack.pop()
            max_area = max(max_area, k[0]* (i-k[1]))
        
        return max_area



