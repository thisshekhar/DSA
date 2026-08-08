class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count  = 0
        current_sum = 0
        prefix_frq = {0:1}
        for num in nums:
            current_sum += num
            target = current_sum  - k
            if(target in prefix_frq):
                count += prefix_frq[target]
            prefix_frq[current_sum] = prefix_frq.get(current_sum,0) + 1
        return count

            
