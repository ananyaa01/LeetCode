class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxx=0
        n,m=len(mat),len(mat[0])
        ind=0
        for i in range(n):
            c=0
            for j in range(m):
                if(mat[i][j]==1):
                    c+=1
            if c>maxx:
                maxx=c
                ind=i
        return [ind,maxx]
            
        