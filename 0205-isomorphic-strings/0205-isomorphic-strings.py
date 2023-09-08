class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        flag = False
        for i in range(0,len(s)):
            if s[i] not in dic and t[i] not in dic.values():
                dic[s[i]] = t[i]
                flag = True
            else:
                if dic.get(s[i]) != t[i]:
                    return False
        return flag
        
          