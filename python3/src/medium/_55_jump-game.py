from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        cur_i = len(nums) - 1
        required_jump = 0

        while cur_i > 0:
            cur_num = nums[cur_i]

            if cur_num >= required_jump:
                required_jump = 0

            required_jump += 1
            cur_i -= 1

        return nums[0] >= required_jump


test_cases = [
    {'nums': [2,3,1,1,4], 'expected': True},
    {'nums': [3,2,1,0,4], 'expected': False},
]

for idx, case in enumerate(test_cases, 0):
    nums = case['nums']
    expected = case['expected']

    res = Solution().canJump(nums)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

