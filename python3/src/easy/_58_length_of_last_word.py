
class Solution:
    def lengthOfLastWord_funcs(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])

    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0

        last_len = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if last_len == 0:
                    continue
                else:
                    break

            last_len += 1

        return last_len


s = "Hello World"
res = Solution().lengthOfLastWord(s)
assert res == 5, res

s = "   fly me   to   the moon  "
res = Solution().lengthOfLastWord(s)
assert res == 4, res

s = "luffy is still joyboy"
assert Solution().lengthOfLastWord(s) == 6

s = "x"
assert Solution().lengthOfLastWord(s) == 1

s = "       "
assert Solution().lengthOfLastWord(s) == 0
