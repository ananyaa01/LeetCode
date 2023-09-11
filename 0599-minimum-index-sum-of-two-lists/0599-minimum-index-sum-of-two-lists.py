import sys
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        Map={}
        minsum=2000
        for i in range(len(list1)) :
            Map[list1[i]]=i
        res=[]    
        
        for i in range(len(list2)):
            if list2[i] in Map:
                sum=i+Map[list2[i]]
                if sum<minsum :
                    minsum=sum
                    res.clear()
                    res.append(list2[i])
                elif sum==minsum:
                    res.append(list2[i])
        return (res)            
                
                
                
        
        
        