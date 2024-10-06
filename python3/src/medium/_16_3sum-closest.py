from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        l_nums = len(nums)
        closest_total = None
        closest_distance = None
        for i_fix in range(l_nums):
            if i_fix > 0 and nums[i_fix] == nums[i_fix-1]:
                continue

            i_left = i_fix+1
            i_right = l_nums-1

            while i_left < i_right:
                total = nums[i_fix] + nums[i_left] + nums[i_right]

                if closest_distance is None or abs(total-target) < closest_distance:
                    closest_total = total
                    closest_distance = abs(total-target)

                if total < target:
                    i_left += 1
                elif total > target:
                    i_right -= 1
                else:
                    return total

        return closest_total

test_cases = [
    {'nums': [1,2,3,4,5,6,7,8,9], 'target': 10,'expected': 10},
    {'nums': [-1,2,1,-4], 'target': 2,'expected': 2},
    {'nums': [0,0,0], 'target': 1,'expected': 0},
]

for idx, case in enumerate(test_cases, 0):
    nums = case['nums']
    target = case['target']
    expected = case['expected']

    res = Solution().threeSumClosest(nums, target)
    assert res == expected, f"Test {idx} failed: {res} != {expected}"

print("All tests passed!")

