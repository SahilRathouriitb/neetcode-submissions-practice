class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        store = []

        def inner(i):
            # base case 
            if i == len(s):
                output.append(store.copy())
                return

            for j in range(i, len(s)):
                if self.ispalindrome(s, i, j):
                    store.append(s[i:j+1])
                    inner(j+1)
                    store.pop()
        inner(0)
        return output

    def ispalindrome(self, arr, low, up):
        while low < up:
            if arr[low] != arr[up]:
                return False
            low += 1
            up -= 1
        return True

    