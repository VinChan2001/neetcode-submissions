class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # 1. Count frequency for every number:

        for num in nums:
            count[num]= count.get(num,0)+1
        
        # 2. freq[i] stores numbers that appeared exactly i times
        freq = [[] for _ in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        #3. start from the highest frequency and collect k numbers
        res = []

        for cnt in range(len(freq)-1, 0, -1):
            for num in freq[cnt]:
                res.append(num)

                if len(res) == k:
                    return res


        