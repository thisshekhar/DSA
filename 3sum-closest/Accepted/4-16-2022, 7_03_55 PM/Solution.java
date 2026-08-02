// https://leetcode.com/problems/3sum-closest

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        Arrays.sort(nums);
        
        int diff = Integer.MAX_VALUE;
        
    int ans = 0;
        
        for(int i = 0; i < nums.length -2; i++)
        {
            int start = i + 1;
            int end = nums.length -1;
            
            while(start < end)
            {
                int sum = nums[i] + nums[start] + nums[end];
                
                 if(Math.abs(sum -target) < diff)
                {
                    diff = Math.abs(sum -target);
                    ans = sum;
                }
                
                
                if(sum > target)
                    end--;
                else
                    start++;
            }
        }
        
        if(ans == Integer.MAX_VALUE)
                return -1;
        else
            return ans;
        
    }
}