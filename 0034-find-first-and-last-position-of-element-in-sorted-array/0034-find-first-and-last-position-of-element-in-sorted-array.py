def binary_search(low,high,condition):
    
    while(low<=high):
        mid=(low+high)//2
        result=condition(mid)
        if result=='found':
            return mid
        elif result=='left':
            high=mid-1
        elif result=='right':
            low=mid+1
    return -1        
            
def last_position(nums,target):
    def condition(mid):
        if nums[mid]==target :
            if mid< len(nums)-1 and nums[mid+1]==target:
                return 'right'
            return 'found'
        elif nums[mid]<target:
            return 'right'
        elif nums[mid]>target:
            return 'left'
    return binary_search(0,len(nums)-1,condition)
    
def first_position(nums,target):
    def condition(mid):
        if nums[mid]==target:
            if mid>0 and nums[mid-1]==target:
                return 'left'
            return 'found'
        elif nums[mid]<target:
            return 'right'
        else:
            return 'left'
    return binary_search(0,len(nums)-1,condition)
            
            
            
def first_last_position(nums,target):
    return first_position(nums,target),last_position(nums,target)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        return first_last_position(nums,target)
        
        