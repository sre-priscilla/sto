class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0:
            return s
        ret, stack = [], []
        i = 0
        # while i < len(s) and s[i] == ' ':
        #     i += 1
        while i < len(s):
            if s[i] != ' ':
                stack.append(s[i])
                i += 1
            else:
                if len(stack) > 0:
                    ret.append(''.join(stack))
                stack.clear()
                while  i < len(s) and s[i] == ' ':
                    i += 1
        if len(stack) > 0:
            ret.append(''.join(stack))
        ret.reverse()
        return ' '.join(ret)

        # s = s.strip()
        # ret, stack = [], []
        # i = 0
        # while i < len(s):
        #     if s[i] != ' ':
        #         stack.append(s[i])
        #         i += 1
        #     else:
        #         ret.append(''.join(stack))
        #         stack.clear()
        #         while  i < len(s) and s[i] == ' ':
        #             i += 1
        # ret.append(''.join(stack))
        # ret.reverse()
        # return ' '.join(ret)


if __name__ == '__main__':
    print(Solution().reverseWords(' hello world! '))
