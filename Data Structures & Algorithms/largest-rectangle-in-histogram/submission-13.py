class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        i = 0
        max_area = 0

        while i < len(heights):

            j = i-1
            k = i+1
            base = 1
            area = 0
            
            while (j >= 0) and heights[j] >= heights[i]:
                    base += 1
                    j -= 1
                
            while (k <len(heights)) and heights[k] >= heights[i]:
                    base += 1
                    k += 1

            area = base * heights[i]
            max_area = max(area, max_area)
            i += 1
        return max_area

