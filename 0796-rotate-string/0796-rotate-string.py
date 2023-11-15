class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n1=len(s)
        n2=len(goal)
        if n1!=n2:
            return False
        q1=[]
        for i in range(n1):
            q1.append(s[i])
        q2=[]
        for i in range(n2):
            q2.append(goal[i])
        k=n2
        
        while(k>=0):
            temp=q2[0]
            q2.pop(0)
            q2.append(temp)
            if(q1==q2):
                return True
            k-=1
        return False
            