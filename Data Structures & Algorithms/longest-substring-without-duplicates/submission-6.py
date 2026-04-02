class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0 

        left = 0
        right = 0

        count = 1
        store = {s[right]}

        while right< len(s)-1:

            right = right + 1

            if s[right] not in store:
                store.add(s[right])

            elif s[right] in store:
                    while True:
                        if s[left] != s[right]:
                             store.remove(s[left])
                             left = left + 1
                        elif s[left] == s[right]:
                             store.remove(s[left])
                             left = left + 1
                             break
                    store.add(s[right])
                        
                
            
            count = max(count, right - left + 1)

        return count
            



            




                
