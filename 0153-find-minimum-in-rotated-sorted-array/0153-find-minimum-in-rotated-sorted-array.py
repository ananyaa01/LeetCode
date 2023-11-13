import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        ans=sys.maxsize
        if nums[low]<=nums[high]:
            return nums[low]
        else:
            while low<=high:
                mid=(low+high)//2
                if nums[low]<=nums[mid]:
                    ans=min(ans,nums[low])
                    low=mid+1
                elif nums[mid]<=nums[high]:
                    ans=min(ans,nums[mid])
                    high=mid-1
        return ans