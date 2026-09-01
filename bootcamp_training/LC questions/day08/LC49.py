#group anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gp = {}
        for w in strs:
            key = "".join(sorted(w))
            if key in gp:
                gp[key].append(w)
            else:
                gp[key] = [w]
        return list(gp.values())