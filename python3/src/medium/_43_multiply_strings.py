
class Solution:
    def multiply_slow(self, num1: str, num2: str) -> str:
        def char_to_num(c):
            return ord(c) - ord("0")

        res = 0
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                n1 = char_to_num(num1[i])
                n2 = char_to_num(num2[j])

                res += n1*n2*pow(10, (len(num1)-1)-i+(len(num2)-1)-j)

        return str(res)

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1 = len(num1)
        len2 = len(num2)
        res_ar = [0 for _ in range(len1+len2)]
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                n1 = int(num1[i])
                n2 = int(num2[j])

                idx = i+j+1
                num = n1*n2+res_ar[idx]

                res_ar[idx] = num % 10
                res_ar[idx-1] += num // 10

        i = 0
        while i < len(res_ar) and res_ar[i] == 0:
            i += 1

        return "".join([str(_) for _ in res_ar[i:]])


res = Solution().multiply(num1 = "2", num2 = "3")
assert res == "6", res

res = Solution().multiply(num1 = "123", num2 = "456")
assert res == "56088", res

res = Solution().multiply(num1 = "123", num2 = "1")
assert res == "123", res

res = Solution().multiply(num1 = "123", num2 = "0")
assert res == "0", res






