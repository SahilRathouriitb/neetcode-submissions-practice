class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mn = 1
        mx = max(piles)

        while mn <= mx:
            
            mid = mn + (mx-mn)//2

            count = 0
            for i in piles:
                count = count + math.ceil(i/mid) 
                if count>h:
                    mn = mid + 1
                    break
            
            if count <= h:
                mx = mid - 1

            

        return mn