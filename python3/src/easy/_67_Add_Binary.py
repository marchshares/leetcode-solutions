class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a, len_b)

        last_carry = 0
        res = ["0" for _ in range(max_len)]
        for i in range(max_len):
            ai,bi = 0,0

            if len_a-1-i >= 0: ai = int(a[len_a-1-i])
            if len_b-1-i >= 0: bi = int(b[len_b-1-i])

            s = ai+bi+last_carry
            ci = s % 2
            last_carry = s // 2

            res[max_len-1-i] = str(ci)
            # print(ai,bi,last_carry, res)

        if last_carry == 1:
            res.insert(0, "1")

        # print(f"Res: {res}")
        return "".join(res)

    def addBinary_optimized(self, a: str, b: str) -> str:
        # a - should has max length
        if len(a) < len(b):
            a,b = b,a

        len_a = len(a)
        len_b = len(b)

        last_carry = 0
        res = ["0" for _ in range(len_a)]

        # simple summing
        for i in range(len_b):
            ai = int(a[len_a-1-i])
            bi = int(b[len_b-1-i])

            s = ai+bi+last_carry
            ci = s % 2
            last_carry = s // 2

            res[len_a-1-i] = str(ci)

        # now we have only a and carry

        # 1. process carry
        curr = len_b
        if last_carry == 1:
            # switch all 1 to 0 (consistently)
            while curr < len_a:
                if a[len_a - 1 - curr] == "1":
                    res[len_a - 1 - curr] = "0"
                    curr += 1
                else:
                    break

            # switch first 0 to 1
            # or add one more if last
            if curr < len_a:
                res[len_a - 1 - curr] = "1"
                curr += 1
            else:
                res.insert(0, "1")

        # 2. process remaining in a
        for i in range(curr, len_a):
            res[len_a - 1 - i] = a[len_a - 1 - i]

        # print(f"Res: {res}")
        return "".join(res)


res = Solution().addBinary(a = "11", b = "1")
assert res == "100", res

res = Solution().addBinary(a = "1010", b = "1011")
assert res == "10101", res

res = Solution().addBinary(a = "111111111111", b = "1")
assert res == "1000000000000", res

res = Solution().addBinary(a = "10000111100", b = "100")
assert res == "10001000000", res

