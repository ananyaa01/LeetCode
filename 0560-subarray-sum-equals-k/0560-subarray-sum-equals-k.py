class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mpp=defaultdict(int)
        prefix_sum=0
        cnt=0
        mpp[0]=1
        for i in range(0,n):
            prefix_sum+=nums[i]
            remove=prefix_sum-k
            cnt+=mpp[remove]
            mpp[prefix_sum]+=1
        return cnt
        