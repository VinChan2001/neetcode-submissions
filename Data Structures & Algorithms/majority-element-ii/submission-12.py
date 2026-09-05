from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        count = defaultdict(int)

        for i in nums:
            count[i]+=1
        
        freq = defaultdict(list)
        
        for i, j in count.items():
            freq[j].append(i)

        keys = [i for i in freq.keys() if i > n]
        l=[]
        for i in keys:
            l.extend(freq[i])
        
        return l


        