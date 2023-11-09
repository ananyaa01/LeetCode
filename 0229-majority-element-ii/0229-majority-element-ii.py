import sys
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        c1=0
        c2=0
        ele1=-sys.maxsize
        ele2=-sys.maxsize
        for i in range(0,len(nums)):
            if(c1==0 and nums[i]!=ele2):
                ele1=nums[i]
                c1+=1
            elif(c2==0 and nums[i]!=ele1):
                ele2=nums[i]
                c2+=1
            elif(nums[i]==ele1):
                c1+=1
            elif(nums[i]==ele2):
                c2+=1
            else:
                c1-=1
                c2-=1
        co1=0
        co2=0
        for i in range(0,len(nums)):
            if(nums[i]==ele1):
                co1+=1
            elif(nums[i]==ele2):
                co2+=1
        print(co1)
        print(co2)
        ls=[]
        # if(len(nums)<3):
        #     return ls
        # if(len(nums)==1):
        #     return nums
        mini=len(nums)//3 +1
        print(mini)
        if(co1>=mini):
            ls.append(ele1)
        if(co2>=mini):
            ls.append(ele2)
        return ls