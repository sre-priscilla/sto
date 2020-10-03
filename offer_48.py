class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ret = 1
        n, _set = len(s), set()
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            if n - i < ret:
                break
            for j in range(i, n):
                if s[j] in _set:
                    break
                else:
                    _set.add(s[j])
                    dp[i][j] = len(_set)
                    ret = max(ret, dp[i][j])
            _set.clear()
        return ret


if __name__ == '__main__':
    s = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(s))
    s = 'bbbbb'
    print(Solution().lengthOfLongestSubstring(s))
    s = 'pwwkew'
    print(Solution().lengthOfLongestSubstring(s))

