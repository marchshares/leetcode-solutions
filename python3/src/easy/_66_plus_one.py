from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        need_inc = False
        i = len(digits)-1
        while i >= 0:
            if digits[i] == 9:
                need_inc = True
                digits[i] = 0
            else:
                need_inc = False
                digits[i] += 1
                break

            i -= 1

        if need_inc:
            digits.insert(0, 1)

        return digits


digits = [1,2,3]
res = Solution().plusOne(digits)
assert res == [1,2,4], res

digits = [4,3,2,1]
res = Solution().plusOne(digits)
assert res == [4,3,2,2], res

digits = [0]
res = Solution().plusOne(digits)
assert res == [1], res

digits = [9]
res = Solution().plusOne(digits)
assert res == [1,0], res

digits = [9,9,9,9]
res = Solution().plusOne(digits)
assert res == [1,0,0,0,0], res


digits = [1,2,9]
res = Solution().plusOne(digits)
assert res == [1,3,0], res
