class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x 
        left = 0 
        right = x//2 

        while left <= right:

            mid = left + (right-left)//2

            if (mid**2) == x or (((mid*mid) < x) and ((mid + 1)**2) > x):
                return mid

            elif ((mid**2) < x) and ((mid + 1)**2) <= x:
                left = mid + 1
            
            elif ((mid**2) > x):
                right = mid - 1
        


        