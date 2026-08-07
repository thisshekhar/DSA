class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert the list to a set for O(1) lookups. 
        # This is the key to achieving O(n) overall time complexity.
        num_set = set(nums)
        longest_streak = 0

        # Iterating over the set is slightly faster as it removes duplicates
        for num in num_set:
            # Only start checking if it's the absolute beginning of a sequence.
            # If num - 1 is in the set, we already counted this sequence!
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Count upwards to find the end of the current consecutive sequence
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # Update our max length found so far
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

