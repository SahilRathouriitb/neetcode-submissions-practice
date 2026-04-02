class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        right = len(s1) - 1
        element = list()
        for i in s1:
            element.append(i)

        element.sort()

        while right < len(s2):
            j = left    
            store = list()
            while j<= right:
              store.append(s2[j])
              j = j + 1

            # Now the store has the elemnts in the window
            # Let's match
            store.sort()
            if store == element:
                return True
            else:
                left = left + 1
                right = right + 1 
        
        return False


        