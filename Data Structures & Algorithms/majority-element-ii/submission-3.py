from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums)/3

        store = defaultdict(int)
        
        for i in nums:
            store[i]+=1
        l=[]
        for i, j in store.items():
            if j>target:
                l.append(i)
        return l
