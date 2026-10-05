class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for i in strs:
            key = [0]*26
            for j in i:
                inc = ord(j)-ord('a')
                key[inc]+=1
            mp[tuple(key)].append(i)
        return list(mp.values())
        