class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if (num -1) not in num_set:
                x = num
                cnt = 1
                while (x+1)  in num_set:
                    cnt = cnt + 1
                    x = x + 1
                longest = max(cnt,longest)
        return longest

