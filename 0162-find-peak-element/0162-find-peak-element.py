class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # n=len(nums)
        # if n==1:
        #     return 0
        # if nums[0]>nums[1]:
        #     return 0
        # if nums[n-1]>nums[n-2]:
        #     return n-1
        # low=1
        # high=n-2
        # while low<=high:
        #     mid=(low+high)//2
        #     if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
        #         return mid
        #     if nums[mid]>nums[mid-1]:
        #         low=mid+1
        #     elif nums[mid]>nums[mid+1]:
        #         high=mid-1
        # return -1
        n = len(nums)  # Size of the array

        # Edge cases:
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2

            # If arr[mid] is the peak:
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid

            # If we are in the left:
            if nums[mid] > nums[mid - 1]:
                low = mid + 1

            # If we are in the right:
            # Or, arr[mid] is a common point:
            else:
                high = mid - 1

        # Dummy return statement
        return -1
            
                    
        