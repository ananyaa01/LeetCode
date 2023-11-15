class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        k=n-1
        for i in range(n//2):
            print(i)
            print(k)
            s[i],s[k]=s[k],s[i]
            k-=1
        