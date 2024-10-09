from typing import List


class Solution:
    def letterCombinations0(self, digits: str) -> List[str]:
        digit_to_letters_map = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }

        def func(i_digit: int, s: str) -> List[str]:
            res = []

            if i_digit < len(digits):
                cur_digit = digits[i_digit]

                for letter in digit_to_letters_map[cur_digit]:
                    res.extend(
                        func(i_digit + 1, s + letter)
                    )
            else:
                return [s]

            return res

        if not digits:
            return []

        return func(0, "")

    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters_map = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }

        def func(i_digit: int, s: str) -> List[str]:
            res = []

            cur_digit = digits[i_digit]
            if i_digit == len(digits)-1:
                return [s+letter for letter in digit_to_letters_map[cur_digit]]

            else:
                for letter in digit_to_letters_map[cur_digit]:
                    res.extend(
                        func(i_digit + 1, s + letter)
                    )

            return res

        if not digits:
            return []

        return func(0, "")


test_cases = [
    {'digits': "23", 'expected': ["ad","ae","af","bd","be","bf","cd","ce","cf"]},
    {'digits': "", 'expected': []},
    {'digits': "2", 'expected': ["a","b","c"]},
]

for idx, case in enumerate(test_cases, 0):
    digits = case['digits']
    expected = case['expected']

    res = Solution().letterCombinations(digits)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

