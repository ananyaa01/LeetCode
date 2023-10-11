class Solution(object):
    def lengthLongestPath(self, input):
        # NOTE : we maintain a dict for collecting key and the length till now
        d={}
        longest=0
        fileList=input.split("\n")
        for i in fileList:
            # directory
            if "." not in i:
                key = i.count("\t") # level of directory
                value = len(i.replace("\t","")) # length after removing '\t'
                d[key]=value
            # file
            else:
                key=i.count("\t")
                ### NOTE :　length of doc (all directory length + doc length + count of '\') 
                length = sum([d[j] for j in d.keys() if j<key]) + len(i.replace("\t","")) + key
                longest=max(longest,length)
        print (d)
        return longest