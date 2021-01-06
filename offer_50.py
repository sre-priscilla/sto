class Solution:
    # def firstUniqChar(self, s: str) -> str:
    #     map = dict()
    #     for ch in s:
    #         map[ch] = map.get(ch, 0) + 1
    #     for ch, _ in map.items():
    #         if map[ch] == 1:
    #             return ch
    #     return ' '

    def firstUniqChar(self, s: str) -> str:
        counter = [0] * 26
        for ch in s:
            counter[ord(ch) - 97] += 1
        for ch in s:
            if counter[ord(ch) - 97] == 1:
                return ch
        return ' '