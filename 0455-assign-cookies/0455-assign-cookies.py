class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        cookie, kid, count = 0, 0, 0
        while cookie < len(s) and kid < len(g):
            if s[cookie] >= g[kid]:
                cookie += 1
                kid += 1
            else:
                cookie += 1
        return kid