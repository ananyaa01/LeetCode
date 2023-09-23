class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        bucket = [[] for _ in range(26)]
        for i, word in enumerate(words):
            bucket[ord(word[0]) - ord('a')].append((i, 0))
        for c in s:
            index = ord(c) - ord('a')
            prevBucket = bucket[index]
            bucket[index] = []
            for i, j in prevBucket:
                j += 1
                if j == len(words[i]):  
                    ans += 1
                else:
                    bucket[ord(words[i][j]) - ord('a')].append((i, j))

        return ans
        