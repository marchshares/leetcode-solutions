from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = dict()

        for i in range(len(nums)):
            cur = nums[i]
            additional = target - cur

            if additional in d:
                return [d[additional], i]
            else:
                d[cur] = i

        return []


test_cases = [
    {'nums': [2, 7, 11, 15], 'target': 9, 'expected': [0, 1]},
    {'nums': [3, 2, 4], 'target': 6, 'expected': [1, 2]},
    {'nums': [3, 3], 'target': 6, 'expected': [0, 1]},
]

for idx, case in enumerate(test_cases, 0):
    nums = case['nums']
    target = case['target']
    expected = case['expected']

    res = Solution().twoSum(nums, target)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

