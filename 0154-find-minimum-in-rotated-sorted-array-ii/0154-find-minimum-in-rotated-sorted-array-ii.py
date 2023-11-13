import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        ans=nums[0]
        if nums[low]<nums[high]:
            return nums[low]
        else:
            while low<=high:
                mid=(low+high)//2
                if(nums[high]==nums[mid]):
                    high-=1
                    
                elif nums[mid]<nums[high]:
                    
                    high=mid
                else:
                    low=mid+1
        return nums[low]