from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        l_nums = len(nums)
        for i_fix in range(l_nums):
            if i_fix > 0 and nums[i_fix] == nums[i_fix - 1]:
                continue

            res_threeSum = self.threeSum(nums, i_fix, target-nums[i_fix])

            res.extend(res_threeSum)

        return res

    def threeSum(self, nums: List[int], i_start_fix: int, target: int) -> List[List[int]]:
        res = []

        l_nums = len(nums)
        for i_fix in range(i_start_fix+1, l_nums):
            if i_fix > i_start_fix+1 and nums[i_fix] == nums[i_fix - 1]:
                continue

            i_left = i_fix + 1
            i_right = l_nums - 1

            while i_left < i_right:
                total = nums[i_fix] + nums[i_left] + nums[i_right]

                if total < target:
                    i_left += 1
                elif total > target:
                    i_right -= 1
                else:
                    res.append(
                        [nums[i_start_fix], nums[i_fix], nums[i_left], nums[i_right]]
                    )

                    i_left += 1
                    while nums[i_left] == nums[i_left - 1] and i_left < i_right:
                        i_left += 1

        return res

test_cases = [
    {'nums': [-2,-2,-2,-2,-1,-1,-1,-1,1,1,1,1,2,2,2,2], 'target': 0,'expected': [[-2, 2, 2, -2], [-1, 1, 2, -2], [-1, 1, 1, -1]]},
    {'nums': [1,0,-1,0,-2,2], 'target': 0,'expected': [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]},
    {'nums': [2,2,2,2,2], 'target': 8,'expected': [[2,2,2,2]]},
]

for idx, case in enumerate(test_cases, 0):
    nums = case['nums']
    target = case['target']
    expected = case['expected']

    res = Solution().fourSum(nums, target)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

