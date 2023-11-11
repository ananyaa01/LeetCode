class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        maxLeft,maxRight=0,0
        res=0
        while left<=right:
            if height[left]<=height[right]:
                if height[left] >= maxLeft:
                    maxLeft=height[left]
                else:
                    res+=maxLeft-height[left]
                left+=1
            else:
                if height[right]>=maxRight:
                    maxRight=height[right]
                else:
                    res+=maxRight-height[right]
                right-=1
        return res            
        
        