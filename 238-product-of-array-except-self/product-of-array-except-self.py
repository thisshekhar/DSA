class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        ans = [1] * n

        #prefix sum
        for i in range(1,n):
            ans[i] = nums[i-1] * ans[i-1]
        
        prevSuffex = 1

        for i in range(n-2, -1, -1):
            prevSuffex *= nums[i+1]
            ans[i] *= prevSuffex
        
        return ans
