# getting the length of longest increasing subsequence in an array | O(n^2) time | dynamic programming | O(n) space | O(n) complexity
def longest_increasing_subsequence(arr):
   n = len(arr)
   if(n ==0):
      return 0
   
   dp = [1] * n

   for i in range(1, n):
      for j in range(i):
         if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

   return max(dp)

# with binary search | O(n log n) time | O(n) space
def longest_increasing_subsequence_bs(arr):
    #from bisect import bisect_left

    n = len(arr)
    if n == 0:
        return 0

    tail = []

    for num in arr:
        #pos = bisect_left(tail, num)
        pos = binary_search(tail, num)
        if pos == len(tail):
            tail.append(num)
        else:
            tail[pos] = num

    return len(tail)

def binary_search(sub, x):
    """Find the index to insert x in sub (lower bound)."""
    left, right = 0, len(sub) - 1
    while left <= right:
        mid = (left + right) // 2
        if sub[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left  # insertion position

# Example usage
if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print("Length of Longest Increasing Subsequence is", longest_increasing_subsequence_bs(arr))   