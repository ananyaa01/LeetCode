class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0 :
            return True
        if len(t)==0 :
            return False
        count=0
        temp=''
        for i in t:
            if count<len(s) and s[count]==i:
                temp+=i
                count+=1
        if temp==s:
            return True
        else:
            return False
        
        