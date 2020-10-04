class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        # ret = 1
        # n, _set = len(s), set()
        # dp = [[0 for i in range(n)] for i in range(n)]
        # for i in range(n):
        #     if n - i < ret:
        #         break
        #     for j in range(i, n):
        #         if s[j] in _set:
        #             break
        #         else:
        #             _set.add(s[j])
        #             dp[i][j] = len(_set)
        #             ret = max(ret, dp[i][j])
        #     _set.clear()
        # return ret

        ret = 0
        if len(s) == 0:
            return ret
        i, n = 0, len(s)

        _map = dict()
        for j in range(n):
            if s[j] in _map:
                i = max(i, _map[s[j]] + 1)
            _map[s[j]] = j
            ret = max(ret, j - i + 1)
        return ret

        # if len(s) == 0:
        #     return 0
        # ret, _set = 0, set()
        # i, j = 0, 0
        # while j < len(s):
        #     if s[j] in _set:
        #         _set.remove(s[i])
        #         i += 1
        #     else:
        #         _set.add(s[j])
        #         j += 1
        #         ret = max(ret, len(_set))
        # return ret





if __name__ == '__main__':
    s = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(s))
    s = 'bbbbb'
    print(Solution().lengthOfLongestSubstring(s))
    s = 'pwwkew'
    print(Solution().lengthOfLongestSubstring(s))

