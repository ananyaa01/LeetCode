import sys
class Solution:
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    sum=0
    start=0
    end=0
    n=len(nums)
    mini=len(nums)+1
    while(end<n):
        while(sum<s and end<n):
            sum+=nums[end]
            end+=1
        while(sum>=s and start<n):
            if(end-start<mini):
                mini=end-start
            sum-=nums[start]
            start+=1
    if mini != len(nums)+1:
        return mini
    else:
        return 0
            
