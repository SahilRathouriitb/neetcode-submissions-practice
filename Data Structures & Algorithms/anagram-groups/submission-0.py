class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            a = "".join(sorted(i))
            if a not in dict:
                dict[a] = []
            
            dict[a].append(i)
        final = []
        for i in dict:
             final.append(dict[i])

        return final
        