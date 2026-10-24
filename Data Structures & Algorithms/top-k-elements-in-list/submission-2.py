from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_dict = defaultdict(int)
        for num in nums:
            bucket_dict[num]+=1
        bucket_list = [[] for _ in range(len(nums)+1)]
        for num in bucket_dict:
            bucket_list[bucket_dict[num]].append(num)
        res=[]; flag=0
        for i in range(len(bucket_list)-1, 0, -1):
            if bucket_list[i] is not []:
                res.extend(bucket_list[i])
                if len(res)>=k: break
        return res[:k]
        
        
        