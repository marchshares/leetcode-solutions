from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        prev_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            if prev_sum <= 0:
                prev_sum = num
            else:
                prev_sum += num

            if prev_sum >= max_sum:
                max_sum = prev_sum

            # print(f"{num}: prev: {prev_sum} max: {max_sum}")

        return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
res = Solution().maxSubArray(nums)
assert res == 6

nums = [1]
res = Solution().maxSubArray(nums)
assert res == 1

nums = [5,4,-1,7,8]
res = Solution().maxSubArray(nums)
assert res == 23
