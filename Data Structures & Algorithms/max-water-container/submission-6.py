class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        i = 0 
        j = len(heights)-1
        while i<j:
            
            k = (j-i)*min(heights[j],heights[i])
            if k>max:
                max = k

            if heights[i]<heights[j]:
                i = i + 1
            elif heights[i]>heights[j]:
                j = j-1
            else:
                i = i+1
                
        return max

