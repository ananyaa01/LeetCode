import sys
class Solution:
    
            
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ele=self.find_max(piles)
        low=1
        high=max_ele-1
        
        while(low<=high):
            mid=(low+high)//2
            hours=self.total_hours(piles,mid)
            if hours<=h:
                high=mid-1
            else:
                low=mid+1
        return low
    def find_max(self,arr):
        maxi=sys.maxsize
        for i in range(len(arr)):
            if arr[i]>maxi:
                maxi=arr[i]
        return maxi
    def total_hours(self,arr,mid):
        hourly=0
        for i in range(len(arr)):
            hourly+=ceil(arr[i]/mid)
        return hourly
    
    
            
            
        