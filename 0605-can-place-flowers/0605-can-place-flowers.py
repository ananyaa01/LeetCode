class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flag=0
        for i in range(len(flowerbed)):
            if i==0:
                if  len(flowerbed)>1:
                    if flowerbed[i]==0 and flowerbed[i+1]==0:
                        flag+=1
                        flowerbed[i]=1
                    
                elif flowerbed[i]==0:
                    flag+=1    
            elif i==(len(flowerbed)-1):
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    flag+=1
                    flowerbed[i]=1        
            elif flowerbed[i]==0 :
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flag+=1
                    flowerbed[i]=1
                
        if flag>=n:
            return True
        else:
            return False         
