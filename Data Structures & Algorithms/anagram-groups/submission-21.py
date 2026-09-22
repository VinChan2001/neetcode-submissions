from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            mp = [0]*26
            j=0
            while j < len(strs[i]):
                key = ord('a') - ord(strs[i][j])
                mp[key]+=1
                j+=1
            d[tuple(mp)].append(strs[i])
        return list(d.values())





        
        