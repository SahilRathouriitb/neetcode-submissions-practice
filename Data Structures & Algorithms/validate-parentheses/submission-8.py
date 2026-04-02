class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(':')','{':'}','[':']',')':'(','}':'{',']':'['}
        l = []
        for i in s:
            if i in {'(','{','['}:
                l.append(i)

            if i in {')','}',']'}:
                if len(l) == 0:
                    return False
                a = l.pop()
                if match[i] != a:
                    return False
                  
        if len(l) != 0:        
            return False
        else:
             return True 