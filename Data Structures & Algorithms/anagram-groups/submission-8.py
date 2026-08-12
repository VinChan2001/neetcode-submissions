class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorted version of solution practice
        sortedS = defaultdict(list)

        for i in strs:
            x = ''.join(sorted(i))
            sortedS[x].append(i)
        
        return list(sortedS.values())
        

            
            

        