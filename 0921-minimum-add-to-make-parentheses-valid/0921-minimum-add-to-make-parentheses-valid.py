class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        cnt=0
        n=len(s)
        for i in range(0,n):
            if s[i]=='(':
                stack.append('(')
            elif s[i]==')':
                if len(stack)==0:
                    cnt+=1
                else:
                    stack.pop()
        if len(stack)==0:
            return cnt
        else:
            while(len(stack)!=0):
                stack.pop()
                cnt+=1
        return cnt
        