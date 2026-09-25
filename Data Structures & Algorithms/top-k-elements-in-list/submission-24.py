class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i]+=1

        freq = [[] for _ in range(len(nums)+1)]

        for i, j in count.items():
            freq[j].append(i)

        res=[]

        for cnt in range(len(freq)-1, 0 , -1):
            for num in freq[cnt]:
                res.append(num)

                if len(res) == k:
                    return res

