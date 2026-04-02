class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mn = 1
        mx = max(piles)
        dct = {}

        while mn <= mx:
            
            mid = mn + (mx-mn)//2

            count = 0
            for i in piles:
                count = count + math.ceil(i/mid) 
                if count>h:
                    mn = mid + 1
                    break
            
            if count <= h:
                dct[mid] = count
                mx = mid - 1

            #print(mid, count, dct)

        return mn