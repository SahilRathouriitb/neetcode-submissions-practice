# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1 
        while left <= n:
            mid = left + (n-left)//2 
            a = guess(mid)
            if a == 0:
                return mid
            elif a == -1:
                n = mid-1
            elif a == 1:
                left = mid + 1
        