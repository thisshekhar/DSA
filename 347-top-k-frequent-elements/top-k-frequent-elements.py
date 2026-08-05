class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        seen = {}
        for num in nums:
                seen[num] = seen.get(num,0) +1
        heap = []
        for num, count in seen.items():
            heapq.heappush(heap,(count,num))
            if(len(heap) > k):
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            if(k> 0):
                res.append(heapq.heappop(heap)[1])
        return res
