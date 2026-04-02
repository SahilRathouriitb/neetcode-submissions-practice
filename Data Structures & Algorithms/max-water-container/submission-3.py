class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):

               k = (j-i) * min(heights[i],heights[j])
               if k>max:
                    max = k

        return max

