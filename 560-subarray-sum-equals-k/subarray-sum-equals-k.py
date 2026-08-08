class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count =- 0
        prefixSum_frq = {0:1}
        current_sum = 0
        for num in nums:
            current_sum += num
            target = current_sum - k
            if(target in prefixSum_frq):
                count += prefixSum_frq[target]
            prefixSum_frq[current_sum] = prefixSum_frq.get(current_sum,0) + 1
        return count
