class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=""
        for i in s:
            if(i.isalpha() or i.isnumeric()):
                str1+=i
       
                
        str1=str1.lower()
        
        if(str1==str1[::-1]):
            return True
        else:
            return False
        