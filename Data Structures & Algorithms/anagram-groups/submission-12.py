class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorted version of solution practice
        # sortedS = defaultdict(list)

        # for i in strs:
        #     x = ''.join(sorted(i))
        #     sortedS[x].append(i)
        
        # return list(sortedS.values())

        # the above solution takes m*nlogn time which is lil bit much
        # we can do this in a much better way
        sortedS = defaultdict(list)

        for i in strs:
            count = [0]*26
            for j in i:
                key = ord(j)-ord('a')
                count[key]+=1
            sortedS[tuple(count)].append(i)

        return list(sortedS.values())
        

            
            

        