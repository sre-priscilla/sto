class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # if len(s) == 0:
        #     return s
        # k = n % len(s)
        # return s[k:] + s[:k]

        k, ret = n % len(s), []
        for i in range(k, len(s)):
            ret.append(s[i])
        for i in range(k):
            ret.append(s[i])
        return ''.join(ret)
