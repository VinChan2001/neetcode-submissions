from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # target = len(nums)/3

        # store = defaultdict(int)
        
        # for i in nums:
        #     store[i]+=1
        # l=[]
        # for i, j in store.items():
        #     if j>target:
        #         l.append(i)
        # return l

        # O(1) space complexity solution:

        count = defaultdict(int)

        for i in nums:
            count[i]+=1

            if len(count)<=2:
                continue
            
            new_count = defaultdict(int)

            for i,j in count.items():
                if j>1:
                    new_count[i]=j-1
            count = new_count

        res=[]
        for i in count:
            if nums.count(i) > len(nums)//3:
                res.append(i)
        return res
                
