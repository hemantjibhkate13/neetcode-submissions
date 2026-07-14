import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_dict = {}

        for num in nums:
            if num in res_dict:
                res_dict[num] += 1
            else:
                res_dict[num] = 1

        top_keys = heapq.nlargest(k, res_dict, key=res_dict.get)

        return top_keys
   