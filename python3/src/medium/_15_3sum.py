from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        l_nums = len(nums)
        for i_fix in range(l_nums):
            if i_fix > 0 and nums[i_fix] == nums[i_fix-1]:
                continue

            i_left = i_fix+1
            i_right = l_nums-1

            while i_left < i_right:
                total = nums[i_fix] + nums[i_left] + nums[i_right]

                if total < 0:
                    i_left += 1
                elif total > 0:
                    i_right -= 1
                else:
                    res.append(
                        [nums[i_fix], nums[i_left], nums[i_right]]
                    )

                    i_left += 1
                    while nums[i_left] == nums[i_left-1] and i_left < i_right:
                        i_left += 1

        return res


test_cases = [
    {'nums': [-1,0,1,2,-1,-4], 'expected': [[-1,-1,2],[-1,0,1]]},
    {'nums': [-1,0,1,2,2,2,-1,-4], 'expected': [[-4,2,2], [-1,-1,2],[-1,0,1]]},
    {'nums': [0,1,1], 'expected': []},
    {'nums': [0,0,0], 'expected': [[0,0,0]]},
]

for idx, case in enumerate(test_cases, 0):
    nums = case['nums']
    expected = case['expected']

    res = Solution().threeSum(nums)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

