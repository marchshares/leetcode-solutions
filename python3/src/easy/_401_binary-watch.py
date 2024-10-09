from typing import List


class Solution:

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        leds_count = 10

        def func(cur_h: int, cur_m: int, left: int, n: int):
            res = []

            for i in range(left, leds_count):
                if i < 6:
                    new_m = cur_m + 2 ** i
                    if new_m >= 60:
                        continue

                    if n > 1:
                        res.extend(
                            func(cur_h, new_m, i + 1, n - 1)
                        )
                    else:
                        new_m_str = str(new_m)
                        if len(new_m_str) == 1:
                            new_m_str = f"0{new_m_str}"

                        res.append(
                            f"{cur_h}:{new_m_str}"
                        )

                if i >= 6:
                    new_h = cur_h + 2 ** (i-6)
                    if new_h >= 12:
                        continue

                    if n > 1:
                        res.extend(
                            func(new_h, cur_m, i + 1, n - 1)
                        )
                    else:
                        cur_m_str = str(cur_m)
                        if len(cur_m_str) == 1:
                            cur_m_str = f"0{cur_m_str}"

                        res.append(
                            f"{new_h}:{cur_m_str}"
                        )

            return res

        n = turnedOn
        if n == 0:
            return ["0:00"]

        return func(0, 0, 0, n)


test_cases = [
    {'turnedOn': 1, 'expected': ["0:01","0:02","0:04","0:08","0:16","0:32", "1:00","2:00","4:00","8:00"]},
    {'turnedOn': 9, 'expected': []},
    {'turnedOn': 3, 'expected': []},
]

for idx, case in enumerate(test_cases, 0):
    turnedOn = case['turnedOn']
    expected = case['expected']

    res = Solution().readBinaryWatch(turnedOn)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

