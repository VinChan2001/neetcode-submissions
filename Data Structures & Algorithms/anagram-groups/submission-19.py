from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        maps = defaultdict(list)
        
        for i in strs:
            k=[0]*26
            j=0
            while j < len(i):
                key = ord('a') - ord(i[j])
                k[key]+=1
                j+=1
            maps[tuple(k)].append(i)
        return list(maps.values())


