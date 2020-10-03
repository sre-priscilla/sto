class Solution:
    def replaceSpace(self, s: str) -> str:
        ret = []
        for i, ch in enumerate(s):
            if ch != ' ':
                ret.append(ch)
            else:
                ret.append('%20')
        return ''.join(ret)