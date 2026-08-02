// https://leetcode.com/problems/3sum-closest

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        Arrays.sort(array);
        
        int ans = Integer.MAX_VALUE;
        
        
        
        for(int i = 0; i < array.length -2; i++)
        {
            int start = i + 1;
            int end = array.length -1;
            
            while(start < end)
            {
                int sum = array[i] + array[start] + array[end];
                
                 if(Math.abs(sum -target) < Math.abs(ans -target))
                {
                    
                    ans = sum;
                }
                
                
                if(sum > target)
                    end--;
                else
                    start++;
            }
        }
        
        return ans;
        
    }
}