class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in strs:
            count=[0]*26
            for j in i:
                key = ord(j)-ord('a')
                count[key]+=1
            d[tuple(count)].append(i)
        return list(d.values())
        